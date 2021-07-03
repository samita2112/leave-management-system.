from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from classroom.forms import UserForm,ManagerProfileForm,AdminProfileForm,EmployeeProfileForm,ManagerProfileUpdateForm,EmployeeProfileUpdateForm,AdminProfileUpdateForm,LeaveCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from classroom import models
from classroom.models import Employee,Manager,Adminn,Leave
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.contrib import messages
import datetime

def ManagerSignUp(request):
    user_type = 'manager'
    registered = False
  
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        manager_profile_form = ManagerProfileForm(data = request.POST)

        if user_form.is_valid() and manager_profile_form.is_valid():

            user = user_form.save()
            user.is_manager = True
            user.save()

            profile = manager_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,manager_profile_form.errors)
    else:
        user_form = UserForm()
        manager_profile_form = ManagerProfileForm()

    return render(request,'classroom/manager_signup.html',{'user_form':user_form,'manager_profile_form':manager_profile_form,'registered':registered,'user_type':user_type})
def AdminSignUp(request):
    user_type = 'admin'
    registered = False
    
    admin=Adminn.objects.all()
    if len(admin)<3:
        if request.method == "POST":
            user_form = UserForm(data = request.POST)
            admin_profile_form = AdminProfileForm(data = request.POST)

            if user_form.is_valid() and admin_profile_form.is_valid():
                vali=False
                user = user_form.save()
                user.is_admin = True
                user.save()

                profile = admin_profile_form.save(commit=False)
                profile.user = user
                profile.save()

                registered = True
            else:
                vali=False
                print(user_form.errors,admin_profile_form.errors)
        else:
            vali=False
            user_form = UserForm()
            admin_profile_form = AdminProfileForm()
    else:
        
        vali=True
        return render(request,'classroom/admin_signup.html',{'registered':registered,'user_type':user_type,'vali':vali})

    return render(request,'classroom/admin_signup.html',{'user_form':user_form,'admin_profile_form':admin_profile_form,'registered':registered,'user_type':user_type,'vali':vali})



def EmployeeSignUp(request):
    user_type = 'employee'
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        employee_profile_form = EmployeeProfileForm(data = request.POST)

        if user_form.is_valid() and employee_profile_form.is_valid():

            user = user_form.save()
            user.is_employee = True
            user.save()

            profile = employee_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,employee_profile_form.errors)
    else:
        user_form = UserForm()
        employee_profile_form = EmployeeProfileForm()

    return render(request,'classroom/employee_signup.html',{'user_form':user_form,'employee_profile_form':employee_profile_form,'registered':registered,'user_type':user_type})


def SignUp(request):
    return render(request,'classroom/signup.html',{})

## login view.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('classroom:login')
    else:
        return render(request,'classroom/login.html',{})

## logout view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

## User Profile 
class EmployeeDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "employee"
    model = models.Employee
    template_name = 'classroom/employee_detail_page.html'

class AdminDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "admin"
    model = models.Adminn
    template_name = 'classroom/admin_detail_page.html'

## User Profile 
class ManagerDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "manager"
    model = models.Manager
    template_name = 'classroom/manager_detail_page.html'
@login_required
def AdminUpdateView(request,pk):
    profile_updated = False
    admin = get_object_or_404(models.Adminn,pk=pk)
    if request.method == "POST":
        form = AdminProfileUpdateForm(request.POST,instance=admin)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            profile_updated = True
    else:
        form = AdminProfileUpdateForm(request.POST or None,instance=admin)
    return render(request,'classroom/admin_update_page.html',{'profile_updated':profile_updated,'form':form})

@login_required
def EmployeeUpdateView(request,pk):
    profile_updated = False
    employee = get_object_or_404(models.Employee,pk=pk)
    if request.method == "POST":
        form = EmployeeProfileUpdateForm(request.POST,instance=employee)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            profile_updated = True
    else:
        form = EmployeeProfileUpdateForm(request.POST or None,instance=employee)
    return render(request,'classroom/employee_update_page.html',{'profile_updated':profile_updated,'form':form})

@login_required
def ManagerUpdateView(request,pk):
    profile_updated = False
    manager = get_object_or_404(models.Manager,pk=pk)
    if request.method == "POST":
        form = ManagerProfileUpdateForm(request.POST,instance=manager)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            profile_updated = True
    else:
        form = ManagerProfileUpdateForm(request.POST or None,instance=manager)
    return render(request,'classroom/manager_update_page.html',{'profile_updated':profile_updated,'form':form})

def allemployee_list(request):
    query = request.GET.get("q", None)
    qs = Employee.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(name__icontains=query)
                )

    context = {
        "employee_list": qs,
    }
    template = "classroom/employee_list.html"
    return render(request, template, context)


## List of all the manager present in the portal.
def manager_list(request):
    query = request.GET.get("q", None)
    qs = Manager.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(name__icontains=query)
                )

    context = {
        "manager_list": qs,
    }
    template = "classroom/manager_list.html"
    return render(request, template, context)
## List of all the admin present in the portal.
def admin_list(request):
    query = request.GET.get("q", None)
    qs = Adminn.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(name__icontains=query)
                )

    context = {
        "admin_list": qs,
    }
    template = "classroom/admin_list.html"
    return render(request, template, context)





## For changing password.
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST , user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed")
            return redirect('home')
        else:
            return redirect('classroom:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'classroom/change_password.html',args)



@login_required
def leave_creation(request):
	if request.method == 'POST':
		form = LeaveCreationForm(data = request.POST)
		if form.is_valid():
            
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			instance.save()
			messages.success(request,'Leave Request Sent,wait for ATA Freight Managers response',extra_tags = 'alert alert-success alert-dismissible show')
			return redirect('classroom:createleave')

		messages.error(request,'failed to Request a Leave,please check entry dates',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('classroom:createleave')


	dataset = dict()
	form = LeaveCreationForm()
	dataset['form'] = form
	dataset['title'] = 'Apply for Leave'
	return render(request,'classroom/create_leave.html',dataset)
	
@login_required
def leaves_list(request):
	leaves = Leave.objects.all_pending_leaves()
	return render(request,'classroom/leaves_recent.html',{'leave_list':leaves,'title':'leaves list - pending'})


@login_required
def leaves_approved_list(request):
	leaves = Leave.objects.all_approved_leaves() #approved leaves -> calling model manager method
	return render(request,'classroom/leaves_approved.html',{'leave_list':leaves,'title':'approved leave list'})


@login_required
def leaves_view(request,id):
	leave = get_object_or_404(Leave, id = id)
	print(leave.user)
	employee = Employee.objects.filter(user = leave.user)[0]
	print(employee)
	return render(request,'classroom/leave_detail_view.html',{'leave':leave,'employee':employee})








@login_required
def approve_leave(request,id):
	leave = get_object_or_404(Leave, id = id)
	user = leave.user
	employee = Employee.objects.filter(user = user)[0]
	leave.approve_leave

	messages.error(request,'Leave successfully approved for {0}'.format(employee.name),extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('classroom:userleaveview', id = id)

@login_required
def cancel_leaves_list(request):
	leaves = Leave.objects.all_cancel_leaves()
	return render(request,'classroom/leaves_cancel.html',{'leave_list_cancel':leaves,'title':'Cancel leave list'})


@login_required
def unapprove_leave(request,id):
	leave = get_object_or_404(Leave, id = id)
	leave.unapprove_leave
	return redirect('classroom:leaveslist') #redirect to unapproved list



@login_required
def cancel_leave(request,id):
	leave = get_object_or_404(Leave, id = id)
	leave.leaves_cancel

	messages.success(request,'Leave is canceled',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('classroom:canceleaveslist')#work on redirecting to instance leave - detail view


# Current section -> here
@login_required
def uncancel_leave(request,id):

	leave = get_object_or_404(Leave, id = id)
	leave.status = 'pending'
	leave.is_approved = False
	leave.save()
	messages.success(request,'Leave is uncanceled,now in pending list',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('classroom:canceleaveslist')#work on redirecting to instance leave - detail view


@login_required
def leave_rejected_list(request):

	dataset = dict()
	leave = Leave.objects.all_rejected_leaves()

	dataset['leave_list_rejected'] = leave
	return render(request,'classroom/rejected_leaves_list.html',dataset)


@login_required
def reject_leave(request,id):
	dataset = dict()
	leave = get_object_or_404(Leave, id = id)
	leave.reject_leave
	messages.success(request,'Leave is rejected',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('classroom:leavesrejected')

	# return HttpResponse(id)

@login_required
def unreject_leave(request,id):
	leave = get_object_or_404(Leave, id = id)
	leave.status = 'pending'
	leave.is_approved = False
	leave.save()
	messages.success(request,'Leave is now in pending list ',extra_tags = 'alert alert-success alert-dismissible show')

	return redirect('classroom:leavesrejected')



#  staffs leaves table user only
@login_required
def view_my_leave_table(request):
	# work on the logics
	if request.user.is_authenticated:
		user = request.user
		leaves = Leave.objects.filter(user = user)
		employee = Employee.objects.filter(user = user).first()
		print(leaves)
		dataset = dict()
		dataset['leave_list'] = leaves
		dataset['employee'] = employee
		dataset['title'] = 'Leaves List'
	else:
		return redirect('accounts:login')
	return render(request,'classroom/staff_leaves_table.html',dataset)



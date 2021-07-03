from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns =[
   path('signup/',views.SignUp,name="signup"),
    path('signup/employee_signup/',views.EmployeeSignUp,name="EmployeeSignUp"),
    path('signup/manager_signup/',views.ManagerSignUp,name="ManagerSignUp"),
    path('signup/admin_signup/',views.AdminSignUp,name="AdminSignUp"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('employee/<int:pk>/',views.EmployeeDetailView.as_view(),name="employee_detail"),
    path('manager/<int:pk>/',views.ManagerDetailView.as_view(),name="manager_detail"),
    path('admin/<int:pk>/',views.AdminDetailView.as_view(),name="admin_detail"),
    path('update/employee/<int:pk>/',views.EmployeeUpdateView,name="employee_update"),
    path('update/admin/<int:pk>/',views.AdminUpdateView,name="admin_update"),
    path('update/manager/<int:pk>/',views.ManagerUpdateView,name="manager_update"),
    path('change_password/',views.change_password,name="change_password"),
    path('employee_list/',views.allemployee_list,name="allemployee_list"),
    path('manager_list/',views.manager_list,name="manager_list"),
    path('admin_list/',views.admin_list,name="admin_list"),
    path('create_leave/',views.leave_creation,name="createleave"),
    path('pending/all/',views.leaves_list,name='leaveslist'),
     path('leaves/view/table/',views.view_my_leave_table,name='staffleavetable'),
    path('all/view/<int:id>/',views.leaves_view,name='userleaveview'),
    path('approve/<int:id>/',views.approve_leave,name='userleaveapprove'),
    path('unapprove/<int:id>/',views.unapprove_leave,name='userleaveunapprove'),
    path('cancel/<int:id>/',views.cancel_leave,name='userleavecancel'),
    path('uncancel/<int:id>/',views.uncancel_leave,name='userleaveuncancel'),
    path('rejected/all/',views.leave_rejected_list,name='leavesrejected'),
    path('reject/<int:id>/',views.reject_leave,name='reject'),
    path('unreject/<int:id>/',views.unreject_leave,name='unreject'),
    path('cancel/all/',views.cancel_leaves_list,name='canceleaveslist'),
    path('approve/all/',views.leaves_approved_list,name='approveleaveslist'),
]

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .form import UserRegisterForm,UserUpdateForm, ProfileUpdateForm
import logging

logger = logging.getLogger(__name__)
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request, 'Account created successifully, You can now Login') 
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'User_Accounts/signup.html', {'form':form})
    
def logout_view(request):
    logout(request)
    messages.info(request,f'You have been logged out Successifuly')
    return redirect('login')
    
@login_required
def profile(request):
    
   if request.method == 'POST': 
      u_form = UserUpdateForm(request.POST ,instance=request.user,)
      p_form = ProfileUpdateForm(request.POST,
                               request.FILES, 
                               instance=request.user.profile)
      if u_form.is_valid() and p_form.is_valid():
        # logger.info('Form is valid. Saving Profile') 
        u_form.save()
        p_form.save()
        messages.success(request, 'Your Account has been updated successifully') 
        return redirect('profile')
    #   else:
    #    logger.error('Form is not valid. Errors : %s', u_form.errors,p_form.errors)
   else:
            
         u_form = UserUpdateForm(instance = request.user)
         p_form = ProfileUpdateForm(instance = request.user.profile)
         
   context = {
            'u_form':u_form,
            'p_form':p_form
          }      
   
   return render(request, 'User_Accounts/profile.html',context)    
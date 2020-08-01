from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name'] # message-name is the name of the input field in the form. u can get the value and pass it in the context dictionary in the view
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			message_name, # subject
			message, #message
			message_email, # email from
			['macnoble306@gmail.com'], # email to you can put a comma and another email address if you want the email to be sent to 2 people

			)
		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


def pricing(request):
	return render(request, 'pricing.html', {})

def about(request):
	return render(request, 'about.html', {})

def services(request):
	return render(request, 'service.html', {})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		appointment = "Name: " + your_name + "Phone: "+ your_phone + "Email: "+ your_email + "Address: "+ your_address + "Schedule: "+ your_schedule + "Day : "+ your_date + "Message: "+ your_message 
		#send email
		send_mail(
			'Appointment request', # subject
			appointment, #message
			your_email, # email from
			['macnoble306@gmail.com'], # email to you can put a comma and another email address if you want the email to be sent to 2 people

			)
		
		return render(request, 'appointment.html',
			{'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message
			},
			)

	else:
		return render(request, 'home.html', {})
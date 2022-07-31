emailbody = ''' 
Hi <recipent>,

I am going to miss <subject> today as I am sick.
Can you please send any work from <subject> that I need to catch up on.

Thanks,
<sender>            
'''
recipent = "Mr A"
subject = "6FAIL9C"
sender = "Myself"

newemailbody = emailbody
newemailbody = newemailbody.replace("<recipent>", recipent)
newemailbody = newemailbody.replace("<subject>", subject)
newemailbody = newemailbody.replace("<sender>", sender)

print(newemailbody)
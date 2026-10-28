#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breachbot.")
userName = input("What is your name?\n")
print("Nice to meet you, " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been", str(timePassed), "years since the Facebook data breach in 2019!")

#Introduces breach
print("Would you like to learn about the 2019 Facebook data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("In 2019, Facebook experienced a data breach that took personal information from 533 million Facebook users and posted it online. Hackers exploited a vulnerability in the feature that allowed users to connect with phone numbers.")
  
  elif topic.lower() == "b":
    print("Facebook found the issue and fixed it, preventing the same method from being used to access data again. The company decided not to notify affected users, reasoning that most of the information exposed was public already and that there were no steps users could take in response.")
  
  elif topic.lower() == "c":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The 2019 Facebook data breach connects to the confidentiality pillar of the CIA Triad, which is about making sure data remains private. However, “malicious actors” that weren’t supposed to have access to the data leaked it for everyone to see.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response because users didn’t even know if their data was stolen or not. At the very least, Facebook should have notified the users it knew were definitely affected so that they could be cautious about potential phishing attacks or similar problems.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by improving their account security in case people try hacking the accounts with the leaked information. My advice would be to check your email with HaveIBeenPwnd, and be wary of scams or fraud.")

  elif topic.lower() == "d":
    break
      
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")

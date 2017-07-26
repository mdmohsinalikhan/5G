no_of_subscribers = 99000
IMSI_space = 10^6


# Graph cars using blue points overlayed by a line 
curve(no_of_subscribers*(1-(1-1/IMSI_space)^x - x*(1/IMSI_space)*(1-1/IMSI_space)^(x-1)), from=0, to=8*10^6, , xlab="no of pseudonyms sent to HN", ylab="expected number of affected users")

# Create a title with a red, bold/italic font
title(main="DoS Attack success", col.main="red", font.main=4)
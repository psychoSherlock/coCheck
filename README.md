# CO-Check

## Simple covid vaccine checker(Indian)
## Checks covid vaccine availabilty without the need of using OTP. It works using the indian cowin api which would fetch vaccine slots without any kind of authentication such as OTP.

#### The script was meant to be checking data on server-side(or backend)
### But unfortunatey, the indian cowin api doesnot allow non-indians to check for vaccines,(and I dont know why).
#### So I had to make it client side. I dont want to handle dynamic urls so I had flask to handle it itself so I dont have to worry

#### You can checkout the server side code on the branch ```server-side```
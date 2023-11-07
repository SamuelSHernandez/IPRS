original = "IFLD,UNPD,TNSF,PR,PRUA,PRIP,PRGC,PRBG,XRED,XDIF,XLSD"
refactored = "IFLD,PR,PRGC,TNSF,UNPD,XDIF,XLSD,XRED,PRIP,PRBG"

codes_o = [code.strip() for code in original.split(",")]
codes_r = [code.strip() for code in refactored.split(",")]

difference = list(set(codes_o) - set(codes_r))

if difference == ['PRUA'] or difference == []:
    print('OK')
else:
    print("Codes that are not the same between the two lists:", difference)

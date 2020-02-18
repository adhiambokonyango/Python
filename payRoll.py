# payRoll calculator

# variable
employeeName = str(input('enter your name'))
hoursWeekly = int(input('enter hours worked in the week '))
hourlyPayRate = 6.75
federalTaxWithholdingRate = 0.2
stateTaxWithholdingRate = 0.09
# end variable

# grossPay
grossPay = hourlyPayRate * hoursWeekly
# end grossPay

# federalTax
federalTaxWithholding = federalTaxWithholdingRate * grossPay
# end federalTax

# state Tax
stateTaxWithholding = stateTaxWithholdingRate * grossPay
# end StateTax

# totalDeduction
totalDeductions = federalTaxWithholding + stateTaxWithholding
# end TotalDeduction

# netPay
netPay = grossPay - totalDeductions
# end NetPay
print('PAYSLIP:')
print('Employee Full Names: ', employeeName)
print('Weekly Hours: ', hoursWeekly)
print('Hourly Pay Rate: $', hourlyPayRate)
print('Gross Pay: $', grossPay)
print('DEDUCTIONS:')
print('Federal Tax WithHolding (20%): $', federalTaxWithholding)
print('State Tax WithHolding (20%):$', stateTaxWithholding)
print('Total Deductions:$', totalDeductions)
print('Net Pay:$', netPay)





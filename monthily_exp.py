m_ex = [2200,2350,2600,2130,2190]
print("In Feb, how many dollars you spent extra compare to jan: ", m_ex[1]- m_ex[0])
print("Total spent in first quarter (first three months): ", sum(m_ex[0:3]))
# for i in m_ex:
#     if i == 2000:
#         print("Did I spent exactly 2000 dollars in any month: ", True)
#     else:
#         print("Did I spent exactly 2000 dollars in any month: ", False)
print("Did I spent exactly 2000 dollars in any month:", 2000 in m_ex)

m_ex.append(1980)

refund = m_ex[3]-200
print("If I am to receive a refund of 200 dollars for this month, how much did I spent this month (substract refund from this month's expense):", refund)
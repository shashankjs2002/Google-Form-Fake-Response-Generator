import requests
import time
import random
fakeLimit = 100

success = 0



while(fakeLimit):

    time.sleep(2)

    # Possible options for each question
    gender_options = ["Male", "Female", "Other", "Prefer not to say"]
    age_options = ["Under 18", "18-25", "25-30", "Above 30"]
    employment_options = ["Employed", "Student", "Not employed but looking for work", "Retired"]
    income_options = ["NIL", "upto Rs. 20,000", "Rs. 20,000- Rs. 50,000", "Rs. 50,000 - Rs. 1,00,000", "above Rs. 1,00,000"]
    location_options = ["Urban", "Rural"]
    premium_options = ["Yes", "No"]
    impact_options = ["A great deal", "A lot", "Moderate Amount", "A little", "None at all"]
    services_options = ["Travel", "News", "OTT", "Health", "Sports", "Dating Apps", "Education", "Music", "Ecommerce", "Food Delivery"]
    rating_options = ["1", "2", "3", "4", "5"]
    frequency_options = ["Weekly", "Monthly", "Quaterly", "Annually", "None"]
    subscription_cost_options = ["NIL", "upto Rs. 1,000", "Rs 1,000- Rs 3,000", "above Rs. 3,000"]
    termination_options = ["Yes", "No"]
    consideration_options = ["Yes", "No", "Maybe"]
    value_options = ["Yes", "No", "Maybe"]
    factors_options = ["Availability of services", "Quality provided in exchange", "Cost of services", "Brand reputation (reliability of service providers)", "Advertisements in between streaming services compel to pay", "Package offers and discounts makes payment of premium profitable","None if not willing to pay"]
    unwilling_options = ["The services have always been free, why should I pay for it now", "They are unreasonably expensive","They don%27t offer many prospects based on the price"]
    pay_again_options = ["Yes", "No"]
    

    # Randomly select options for each question
    gender = random.choice(gender_options).replace(" ", "+")
    age = random.choice(age_options).replace(" ", "+")
    employment_status = random.choice(employment_options).replace(" ", "+")
    income = random.choice(income_options).replace(" ", "+")
    location = random.choice(location_options).replace(" ", "+")
    paid_premium = random.choice(premium_options).replace(" ", "+")
    impact = random.choice(impact_options).replace(" ", "+")
    services_paid_for = random.sample(services_options, random.randint(1, len(services_options)))
    ratings = {service: random.choice(rating_options) for service in services_options}
    frequency_ratings = {service: random.choice(rating_options) for service in services_options}
    payment_plan = random.choice(frequency_options).replace(" ", "+")
    subscription_cost = random.choice(subscription_cost_options).replace(" ", "+")
    terminated_subscription = random.choice(termination_options).replace(" ", "+")
    considered_payment = random.choice(consideration_options).replace(" ", "+")
    value_for_money = random.choice(value_options).replace(" ", "+")
    factors_influencing_decision = random.sample(factors_options, random.randint(1, len(factors_options)))
    unwilling_reasons = random.sample(unwilling_options, random.randint(1, len(unwilling_options)))
    pay_again = random.choice(pay_again_options).replace(" ", "+")

    # Format the responses
    responses = [gender, age, employment_status, income, location, paid_premium, impact,
                ",".join(services_paid_for), ",".join(ratings.values()), ",".join(frequency_ratings.values()),
                payment_plan, subscription_cost, terminated_subscription, considered_payment, value_for_money,
                ",".join(factors_influencing_decision), ",".join(unwilling_reasons), pay_again]

    # Print the responses
    # print(";".join(responses))


    formId ="1FAIpQLScL5KCWjmKktbxOnjOWsZhWIcBZRF2Qtm3hLg2y1UZfps4tBg"

    url = f"""https://docs.google.com/forms/d/e/{formId}/formResponse?usp=pp_url&entry.650296196={gender}&entry.544810109={age}&entry.1201543297={employment_status}&entry.820164872={income}&entry.1674542029={location}&entry.1745863747={paid_premium}&entry.2023527713={impact}"""

    # print(factors_influencing_decision)


    rating_values=list(ratings.values())
    frequency_values = list(frequency_ratings.values())

    for service in services_paid_for:
        url = url + f"&entry.889207627={service}"

    url = url + f"""&entry.1925226833={rating_values[0]}&entry.1537160877={rating_values[1]}&entry.615966007={rating_values[2]}&entry.715254698={rating_values[3]}&entry.1973317110={rating_values[4]}&entry.1512222729={rating_values[5]}&entry.1380642043={rating_values[6]}&entry.254160398={rating_values[7]}&entry.1408732552={rating_values[8]}&entry.1262774076={rating_values[9]}&entry.917320491={frequency_values[0]}&entry.1344888061={frequency_values[1]}&entry.900890462={frequency_values[2]}&entry.1085558857={frequency_values[3]}&entry.65893357={frequency_values[4]}&entry.638585290={frequency_values[5]}&entry.180252766={frequency_values[6]}&entry.1606558438={frequency_values[7]}&entry.830862149={frequency_values[8]}&entry.95027391={frequency_values[9]}&entry.1250814705={payment_plan}&entry.1974160072={subscription_cost}&entry.2041116804={terminated_subscription}&entry.2093578165={considered_payment}&entry.459301991={value_for_money}&entry.46355981={pay_again}"""
    for factor in factors_influencing_decision:
        url = url + f"""&entry.41720957={factor.replace(" ", "+")}"""
    for factor in unwilling_reasons:
        url = url + f"""&entry.508845237={factor.replace(" ", "+")}"""


    # print(url)


    # Replace 'your_endpoint_url' with the actual URL of the endpoint you want to access
    # endpoint_url = 'your_endpoint_url'



    time.sleep(2)
    # Send a GET request
    response = requests.get(url)

    # print(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print("Response Content:", response.status_code)
        success = success +1
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)


    fakeLimit = fakeLimit -1
    time.sleep(1)

print("Total Success: " , success)

url = f"""https://docs.google.com/forms/d/e/1FAIpQLScL5KCWjmKktbxOnjOWsZhWIcBZRF2Qtm3hLg2y1UZfps4tBg/viewform?usp=pp_url&entry.650296196=Male&entry.544810109=Under+18&entry.1201543297=Employed&entry.820164872=upto+Rs.+20,000&entry.1674542029=Urban&entry.1745863747=Yes&entry.2023527713=A+lot&entry.889207627=OTT&entry.889207627=Health&entry.889207627=Sports&entry.1925226833=1&entry.1537160877=2&entry.615966007=3&entry.715254698=4&entry.1973317110=5&entry.1512222729=1&entry.1380642043=2&entry.254160398=3&entry.1408732552=2&entry.1262774076=2&entry.917320491=1&entry.1344888061=2&entry.900890462=3&entry.1085558857=4&entry.65893357=5&entry.638585290=1&entry.180252766=2&entry.1606558438=3&entry.830862149=4&entry.95027391=3&entry.1250814705=Quaterly&entry.1974160072=upto+Rs.+1,000&entry.2041116804=Yes&entry.2093578165=No&entry.459301991=No&entry.41720957=Cost+of+services&entry.41720957=Brand+reputation+(reliability+of+service+providers)&entry.41720957=Advertisements++in+between+streaming+services+compel+to+pay&entry.508845237=They+are+unreasonably+expensive&entry.508845237=They+don't+offer+many+prospects+based+on+the+price&entry.46355981=Yes"""

# url = f"""https://docs.google.com/forms/d/e/{formId}/viewform?usp=pp_url&entry.650296196={gender}&entry.544810109={age}&entry.1201543297={employment_status}&entry.820164872={income}&entry.1674542029={location}&entry.1745863747={paid_premium}&entry.2023527713={impact}&entry.889207627=Travel&entry.889207627=News&entry.1925226833=1&entry.1537160877=2&entry.615966007=2&entry.715254698=2&entry.1973317110=1&entry.1512222729=1&entry.1380642043=1&entry.254160398=2&entry.1408732552=2&entry.1262774076=2&entry.917320491=1&entry.1344888061=1&entry.900890462=1&entry.1085558857=1&entry.65893357=1&entry.638585290=1&entry.180252766=1&entry.1606558438=1&entry.830862149=1&entry.95027391=1&entry.1250814705=Monthly&entry.1974160072=Rs+1,000-+Rs+3,000&entry.2041116804=No&entry.2093578165=Yes&entry.459301991=Maybe&entry.41720957=Quality+provided+in+exchange&entry.41720957=Brand+reputation+(reliability+of+service+providers)&entry.41720957=Advertisements++in+between+streaming+services+compel+to+pay&entry.508845237=They+are+unreasonably+expensive&entry.508845237=They+don%27t+offer+many+prospects+based+on+the+price&entry.46355981=No"""

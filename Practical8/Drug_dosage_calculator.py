def drug_dosage(a,b):#create the function called drug_dosage
    if a<10 or a>100:#return and remind the false type
        return("weight should be between 10 to 100")#raise ValueError
    if b=="120mg/5ml":
        volume=(15*a/120)*5#"15*a" to calculate the required drug dosage(in mg)
    elif b=="250mg/5ml":
        volume=(15*a/250)*5
    else:#return and remind the false type
        return("The concentration of paracetamol should be either 120mg/5ml or 250mg/5ml.")
    return volume
#an example to input
weight=30
con="120mg/5ml"
re=drug_dosage(weight,con)
print(re)        
#list of lambda fxns tns - kgs, kgs - gms, gms - mg, mg-pnds

tonn_weight=float(input("Enter your weight  tonns: "))

weights = [
    lambda tonn_weight: tonn_weight*1000,
    lambda kg:kg*1000,
    lambda gm:gm*1000,
    lambda mg:mg*2.204

]

kg=weights[0](tonn_weight)
gm=weights[1](kg)
mg=weights[2](gm)
lbs=weights[3](mg)

print(f"{tonn_weight} tonns is {kg} kgs, {gm} gms, {mg} mg and {lbs} lbs")
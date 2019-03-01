from src.bayesdice import BayesDice

bd = BayesDice()
bd.choose_die()

for _ in range(3):
    roll = bd.roll_die()
    bd.update_priors(roll)

print('-' * 50)
ans = max(bd.prior.keys(), key=(lambda k: bd.prior[k]))
print('experimental ans is {} and actual ans is {}'.format(ans, bd.die))

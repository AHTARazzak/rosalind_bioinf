the_pop_file = input("Name of file please: ")

pop_file = open(the_pop_file, 'r')

break_numbers = pop_file.read().split()

hom_dom = int(break_numbers[0])
hetero = int(break_numbers[1])
hom_rec = int(break_numbers[2])

pop_size = hom_dom + hetero + hom_rec

if hom_dom > 0:
	dom = (hom_dom/pop_size)

if (hetero > 0) and (hom_dom > 0):
	hetero_dom = (hetero/pop_size) * (hom_dom/(pop_size-1))

if (hetero > 0) and (hom_rec > 0):
	hetero_dom_rec = 0.5 * ((hetero/pop_size) * (hom_rec/(pop_size-1)))

if hetero > 1:
	hetero_hetero = 0.75 * ((hetero/pop_size) * ((hetero-1)/(pop_size-1)))

if (hom_rec > 0) and (hom_dom > 0):
	hom_rec_dom = (hom_rec/pop_size) * (hom_dom/(pop_size-1))

print("%.5f" % (dom + hetero_dom + (2*hetero_dom_rec) + hetero_hetero + hom_rec_dom))
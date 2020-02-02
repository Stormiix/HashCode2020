import glob
import re

regex = r"inputs\\(.*)\.in"
files = glob.glob("inputs\*.in")

for file in files:

    filename = re.search(regex, file).group(1)

    with open('inputs/'+filename+'.in') as inputFile:
        maxSlices, uniquePizzaCount = [
            int(v) for v in inputFile.readline().split(" ")]
        sliceCountPerPizzaType = [int(v)
                                  for v in inputFile.readline().split(" ")]

    pizzas = {pizzaType: slicesPerPizza for pizzaType,
              slicesPerPizza in enumerate(sliceCountPerPizzaType)}
    orderedPizzas = {k: v for k, v in sorted(
        pizzas.items(), reverse=True, key=lambda item: item[1])}
    result = []

    def solution(slices, pizzaTypes=orderedPizzas.copy()):
        """ 1,505,004,318 score solution """
        results = []
        slicesLeft = slices
        stop = False
        while slicesLeft > 0 and not stop:
            ptype = None
            for pizzaType, slicesPerPizza in pizzaTypes.items():
                # print("Type: {}, Slices: {}".format(pizzaType, slicesPerPizza))
                if slicesPerPizza == slices:
                    results += [pizzaType]
                    stop = True
                    continue
                if slicesPerPizza < slicesLeft:
                    ptype = (pizzaType, slicesPerPizza)
                    break
            if not ptype:
                stop = True
                print("Reached the end {} slices left".format(slicesLeft))
                continue
            else:
                # print("Type: {}, Slices: {}, Slices Left: {}".format(ptype[0], ptype[1], slices - ptype[1]))
                del pizzaTypes[ptype[0]]
                results += [ptype[0]]
                slicesLeft -= ptype[1]
        return results

    result = solution(maxSlices)

    # outputPizzas = sorted(result, key=lambda pizzaType: sliceCountPerPizzaType.index(orderedPizzas[pizzaType]))
    finalPizzaTypeCount = len(result)
    outputPizzas2 = sorted(result)

    with open("outputs/{}.out".format(filename), 'w') as output:
        output.write(str(finalPizzaTypeCount)+"\n")
        output.write(" ".join([str(v) for v in outputPizzas2]))

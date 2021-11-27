import json

def run():
    # loading data
    this = open('./stories.json')
    data = json.load(this)

    # variables i'll need to use later
    allnums = []
    responses = []
    common = []
    units = []
    top_unit = ''
    count = 0
    possible = ['place', 'adjective', 'noun']

    # sorting the data to do analytics
    for a in data:
        count += 1
        for b, c in a.items():
            if b == 'number':
                allnums.append(int(c))
            elif b == 'unit':
                units.append(c)
            elif b in possible:
                responses.append(c)
            else:
                pass

    allnums.sort()

    # find the max and min numbers
    maximus = allnums[-1]
    minimus = allnums[0]

    # figure out the top unit used
    top_unit = max(units, key=units.count)

    # find the most common occurences
    for sample in set(responses).intersection(responses):
        common.append(sample)

    print("");print("")
    print("##########################")
    print("STATISTICS ON STORY INPUTS")
    print("##########################")
    print("");print("")
    print(f"Stories: {count} total \nTop Unit: {top_unit} \nMinimum: {minimus} \nMaximum: {maximus} \nCommon Responses: {common}")
    print("");print("")

run()
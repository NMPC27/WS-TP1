#open test.json and count the number of shows

import json
dict = json.loads(open('test.json').read())

print("We have", len(dict), "shows in our database")

#open images.csv and count the number of lines

f=open('images.csv','r')
noimage=0
imageset = set()
for line in f:
    if line.split("> <")[0] not in imageset:
        if "NO_IMAGE" in line:
            noimage+=1
    imageset.add(line.split("> <")[0])

print(f"we have {len(imageset)} different shows in images.csv, {noimage} of them have no image, {len(imageset)-noimage} of them have an image")


validimages = []
for show in imageset:
    validimages.append(show.split("/show/s")[1].split(">")[0])
validimages = sorted([int(i) for i in validimages])
if  validimages == [i for i in range(1,8808)]:
    print("all ids are valid")


#do the same for ratings.csv

f=open('ratings.csv','r')
norating=0
ratingsset = set()

for line in f:
    if line.split("> <")[0] not in ratingsset:
        if "N/A" in line:
            norating+=1
    ratingsset.add(line.split("> <")[0])

print(f"we have {len(ratingsset)} different shows in ratings.csv, {norating} of them have no rating, {len(ratingsset)-norating} of them have a rating")

validratings = []
for show in ratingsset:
    validratings.append(show.split("/show/s")[1].split(">")[0])
validratings = sorted([int(i) for i in validratings])
if  validratings == [i for i in range(1,8808)]:
    print("all ids are valid")

#do the same for trailers.csv

f=open('trailers.csv','r')
notrailer=0
trailersset = set()

for line in f:
    if line.split("> <")[0] not in trailersset:
        if "N/A" in line:
            notrailer+=1
    trailersset.add(line.split("> <")[0])


print(f"we have {len(trailersset)} different shows in trailers.csv, {notrailer} of them have no trailer, {len(trailersset)-notrailer} of them have a trailer")

validtrailers = []
for show in trailersset:
    validtrailers.append(show.split("/show/s")[1].split(">")[0])
validtrailers = sorted([int(i) for i in validtrailers])
if  validtrailers == [i for i in range(1,8808)]: 
    print("all ids are valid")    

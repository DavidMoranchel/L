#different ways to make a dictionary

a = dict(name='David',age=19,country='Mexico')
b = { 
	'name':'David',
	'age':19, 
	'country':'Mexico'
}
c = dict(zip(['name','age','country'],['David',19,'Mexico']))
d = dict([('name','David'),('age',19),('country','Mexico')])
e = dict( { 
	'name':'David',
	'age':19, 
	'country':'Mexico'
})

print(a==b==c==d==e)
#True :)
l =[a,b,c,d,e]
for elements in l:
	print(elements)
# littlebook

## type

- play
  - intro
  - act
    - scene
    - epilogue
- fiction
  - preface/introduction
  - chapters
  - part
    - chapter
- short stories
  - stories
-  essay
  - essay
    - chapter
- poems
  - number
- non-fiction
  - h1, h2, h3 (无固定结构/名称)
- speeches





数据结构

workLink = [link1, link2, link3]

work1 # fiction

work1 = { chap0: '....long text ....', chap1:'.....' }

or

```python
class Entity.
work1 = new entity()

work1.name = 'booksName'
work1.contents = [entity1, entity2, ...]

entity1.name = 'part0'
entity1.contents = [subentity1, subentity2, ...]
entity1.text = ""
subentity1.name = 'chapter1'
subentity1.text =  ['para1','para2', ... ]

q:find chapter1
    for work in work1: work.name = chapter1?
   if not: for work in work1.contents : work.name = chpter1?
        

```

or:

```
work1 = { 'part0' : {
        			'chapter1': {
        				text:[para1, para2, para3....],
        				link:'',
        				pageBegin: 0,
        				PageEnd: 1}
            		'chapter2': '..........'
         },
         'part1':{
             'chapter1':'..........'
         }

}
```







## genre

![](genre.JPG)








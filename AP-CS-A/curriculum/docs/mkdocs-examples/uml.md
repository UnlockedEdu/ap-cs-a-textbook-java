# Markdown Examples
All common Markdown is supported by MkDocs. Supported diagrams are shown with examples below.

## Sequence Diagram
[js-sequence-diagrams](https://bramp.github.io/js-sequence-diagrams/) documentation and live editor

~~~
```sequence
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
```
~~~

```sequence
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
```

## Flow Chart
[flowchart.js](http://flowchart.js.org/) documentation and live editor

~~~
```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```
~~~

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

class Figure:
    type_fig = 'ellipse'
    color = 'red'

    
fig1 = Figure()
setattr(fig1, "start_pt", (10, 5))
setattr(fig1, "end_pt", (100, 20))
setattr(fig1, "color", "blue")

delattr(fig1, "color")

print(*fig1.__dict__)
#
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
#
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'
#
# del fig1.color
#
# [print(i, end=' ') for i in fig1.__dict__]

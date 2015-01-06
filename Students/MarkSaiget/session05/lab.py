#! /usr/mnt/env python


def fourOp(foreground_color='black', background_color='white',
           link_color='blue', visited_link_color='red'):
    print "foreground_color={one}, background_color={two}, link_color={three}, visited_link_color={four}".\
        format(one=foreground_color, two=background_color, three=link_color,
               four=visited_link_color)

if __name__ == '__main__':
    fourOp()
    fourOp(foreground_color='blue')
    fourOp(foreground_color='blue', background_color='pink')
    nonDefault = {'foreground_color': 'pink', 'background_color': 'pink',
                  'link_color': 'pink', 'visited_link_color': 'pink'}
    fourOp(**nonDefault)

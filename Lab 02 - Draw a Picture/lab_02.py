import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Draw A Picture")
arcade.set_background_color(arcade.csscolor.PAPAYA_WHIP)
arcade.start_render()

# Drawing Code Goes Here
# Base trim
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 30, 0, arcade.csscolor.GRAY)
# TV legs
arcade.draw_arc_filled(160 -1, 215, 100, 50, arcade.csscolor.DIM_GRAY, 30, 50, 20)
arcade.draw_arc_filled(545 -1, 215, 100, 50, arcade.csscolor.DIM_GRAY, 30, 50, -240)
# TV stand base colorr
arcade.draw_rectangle_filled((SCREEN_WIDTH - 1) // 2, 120, 500, 200,arcade.csscolor.PERU)
arcade.draw_rectangle_filled(120 - 1, 20, 20, 60,arcade.csscolor.PERU)
arcade.draw_rectangle_filled(580 - 1, 20, 20, 60,arcade.csscolor.PERU)
# TV stand shelves
arcade.draw_rectangle_filled((SCREEN_WIDTH - 1) // 2, 70, 200, 80, arcade.csscolor.SADDLE_BROWN)
arcade.draw_rectangle_filled((SCREEN_WIDTH - 1) // 2, 150, 200, 50, arcade.csscolor.SADDLE_BROWN)
# TV stand cabinet handles
arcade.draw_rectangle_filled((SCREEN_WIDTH - 251) // 2, 130, 10, 50, arcade.csscolor.LIGHT_SLATE_GRAY)
arcade.draw_rectangle_filled((SCREEN_WIDTH + 249) // 2, 130, 10, 50, arcade.csscolor.LIGHT_SLATE_GRAY)
# TV
arcade.draw_rectangle_filled((SCREEN_WIDTH - 1) // 2, 340, 400, 200,arcade.csscolor.DARK_GRAY)
arcade.draw_rectangle_filled((SCREEN_WIDTH - 1) // 2, 340, 380, 180,arcade.csscolor.DARK_SLATE_GRAY)


arcade.finish_render()

arcade.run()
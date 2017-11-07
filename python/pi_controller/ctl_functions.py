import sys, pygame, pygame.midi

def check_slider(slider, mouse_x, mouse_y):
    knob_clicked = slider.rect.collidepoint(mouse_x, mouse_y)
    if knob_clicked:
        slider.k_moving = True

def check_button(button, panels, mouse_x, mouse_y):
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        button.update()
        if button.title == 'Bandpass':
            if button.on == True: # is this best way to do this?
                bandpass_automation(panels)
            elif button.on == False:
                allpass_automation(panels)
        if button.title == 'Mic':
            if button.on == True:
                mic_on_off_automation(panels, 100) # turn mic on
            elif button.on == False:
                mic_on_off_automation(panels, 0) # turn off


def check_events(ctl_settings, screen, panels, buttons, midi_input,
                 ternary_chain, mouse_x, mouse_y):
    # factor all this shit out
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Goodbye')
            #midi_input.close()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print('Goodbye')
                #midi_input.close()
                sys.exit()
            elif event.key == pygame.K_1:
                ctl_settings.panel = 0
            elif event.key == pygame.K_2:
                ctl_settings.panel = 1
            elif event.key == pygame.K_3:
                ctl_settings.panel = 2
            elif event.key == pygame.K_4:
                ctl_settings.panel = 3
            elif event.key == pygame.K_5:
                ctl_settings.panel = 4
            elif event.key == pygame.K_6:
                ctl_settings.panel = 5
            elif event.key == pygame.K_7:
                ctl_settings.panel = 6
            elif event.key == pygame.K_8:
                ctl_settings.panel = 7
            elif event.key == pygame.K_b:
                bandpass_automation(panels)


        # Mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for panel in panels:
                for slider in panel.sliders:
                    check_slider(slider, mouse_x, mouse_y)
            for button in buttons:
                check_button(button, panels, mouse_x, mouse_y)
        elif event.type == pygame.MOUSEBUTTONUP:
            for panel in panels:
                for slider in panel.sliders:
                    slider.k_moving = False

def bandpass_automation(panels):
    print("bandpass automation") # reduce this to for loop, and scale values!
    # wall 1
    panels[0].sliders[1].automate(0)
    panels[0].sliders[2].automate(12.5)
    # wall 2
    panels[1].sliders[1].automate(12.5)
    panels[1].sliders[2].automate(25)
    # wall 3
    panels[2].sliders[1].automate(25)
    panels[2].sliders[2].automate(37.5)
    # wall 4
    panels[3].sliders[1].automate(37.5)
    panels[3].sliders[2].automate(50)
    # wall 5
    panels[4].sliders[1].automate(50)
    panels[4].sliders[2].automate(62.5)
    # wall 6
    panels[5].sliders[1].automate(62.5)
    panels[5].sliders[2].automate(75)
    # wall 7
    panels[6].sliders[1].automate(75)
    panels[6].sliders[2].automate(87.5)
    # wall 8
    panels[7].sliders[1].automate(87.5)
    panels[7].sliders[2].automate(100)

def allpass_automation(panels):
    print("bandpass automation") # reduce this to for loop, and scale values!
    # wall 1
    panels[0].sliders[1].automate(0) # should def be able to do this with for loop
    panels[0].sliders[2].automate(100)
    # wall 2
    panels[1].sliders[1].automate(0)
    panels[1].sliders[2].automate(100)
    # wall 3
    panels[2].sliders[1].automate(0)
    panels[2].sliders[2].automate(100)
    # wall 4
    panels[3].sliders[1].automate(0)
    panels[3].sliders[2].automate(100)
    # wall 5
    panels[4].sliders[1].automate(0)
    panels[4].sliders[2].automate(100)
    # wall 6
    panels[5].sliders[1].automate(0)
    panels[5].sliders[2].automate(100)
    # wall 7
    panels[6].sliders[1].automate(0)
    panels[6].sliders[2].automate(100)
    # wall 8
    panels[7].sliders[1].automate(0)
    panels[7].sliders[2].automate(100)

def mic_on_off_automation(panels, gain_val):
    print("Mic on/off")
    for panel in panels:
        panel.sliders[0].automate(gain_val)

"""
    if midi_input.poll():
        ctl, val = mf.get_ctl_and_value(midi_input)
        #print(ctl)

        if ctl_settings.ternaryWallMode:
            if ctl < 7:
                mf.midi_to_ternary(ternary_chain, ctl, val)
            if ctl == 41 and val == 127:
                print(ternary_chain)
                freqs = of.convert_chain_to_freqs(ternary_chain, ctl_settings)
                print(freqs)
                # add call to function to convert to freq and send to walls
"""

def update_screen(ctl_settings, screen, panels, buttons, mouse_y):

    screen.fill(ctl_settings.bg_color)

    panels[ctl_settings.panel].update(mouse_y)

    for button in buttons:
        button.draw_button()

    pygame.display.flip()
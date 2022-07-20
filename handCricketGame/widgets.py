screens = '''
ScreenManager:
    id: screen_manager
    Mainscreen:
    PlayGameScreen:
    HowToPlay:
    Aboutscreen:
    Statistics:
    Toss:
    TossSelection:
    PlayGame:
    PlayGame2:
    
            
<Mainscreen>:
    name: "Screen0"
    Image:
        source: "Cricket fever.jpg"
        allow_stretch: True
        
    MDLabel:
        text: "HAND CRICKET game"
        halign: "center"
        font_style: "H2"
        pos_hint: {'center_x':0.5, 'center_y':0.9}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1   

    MDRectangleFlatButton:
        text: "How To Play?"
        font_size: 50
        theme_text_color: "Custom"
        text_color: 0,0,0, 1
        line_color: 0, 0, 0, 1
        pos_hint: {'center_x':0.5, 'center_y':0.70}
        size_hint: (0.23, 0.08)
        on_release:
            root.manager.current = 'Screen3'
            root.manager.transition.direction = "right"
            
        
    MDRectangleFlatButton:
        id: PlayGame
        text: "Play Game"
        font_size: 50
        theme_text_color: "Custom"
        text_color: 0,0,0, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.50}
        size_hint: (0.23, 0.08)
        on_release: 
            root.run()
            
    MDRectangleFlatButton:
        text: "Statistics"
        font_size: 50
        theme_text_color: "Custom"
        text_color: 0,0,0, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.30}
        size_hint: (0.23, 0.08)
        on_release: 
            root.manager.current = 'stats'
            root.manager.transition.direction = "up"
            
    MDRectangleFlatButton:
        text: "About"
        font_size: 50
        theme_text_color: "Custom"
        text_color: 0,0,0, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.10}
        size_hint: (0.23, 0.08)
        on_release: 
            root.manager.current = 'about'
            root.manager.transition.direction = "down"
    
        
<PlayGameScreen>:
    name: "Screen2"
    playerName: playerName
    
    Image:
        source: "bat.jpg"
        allow_stretch: True
    
    MDLabel:
        id: player
        text: "HAND CRICKET game"
        halign: "center"
        font_style: "H2"
        pos_hint: {'center_x':0.5, 'center_y':0.9}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    
    MDTextField:
        id: playerName
        hint_text: "Enter your name"
        pos_hint: {'center_x':0.5, 'center_y':0.75}
        size_hint: (0.20, 0.09)
        color_mode: 'custom'
        line_color_focus: 220/255,20/255,60/255,1
        icon_right: "cricket"
        icon_right_color: app.theme_cls.primary_color
        
    
    MDRoundFlatButton:
        text: "Continue"
        font_size: 30
        text_color: 0,0,0, 1
        pos_hint: {'center_x':0.5, 'center_y':0.65}
        size_hint: (0.12, 0.06)
        on_release:
            root.Name_MDDialog()
            
    
    
    
    MDFillRoundFlatButton:
        text: "Back"
        font_size: 20
        pos_hint: {'center_x':0.20, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "right"
            
<HowToPlay>:
    name: 'Screen3'
    Image:
        source: "batball.jpg"
        allow_stretch: True
        
    MDRectangleFlatButton:
        id: howToplay
        text: "Press me!"
        pos_hint: {'center_x':0.50, 'center_y':0.90}
        size_hint: 0.12, 0.12
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        line_color: 0, 0, 0, 1
        disable: False
        on_release:
            root.run()
        
    ScrollView:
        do_scroll_x: True
        do_scroll_y: True
        
        MDLabel:
            id: PlayScroll
            text: " ABC "
            font_size: 50
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]
        
    MDFillRoundFlatButton:
        text: "Back"
        font_size: 20
        pos_hint: {'center_x':0.20, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "left"
            
            
            
<Aboutscreen>:
    name: 'about'
    Image:
        source: "Screen 4.jpg"
        allow_stretch: True
        
    MDRectangleFlatButton:
        text: "Screen4"
        font_size: 50
        theme_text_color: "Custom"
        text_color: 135/255,206/255,235/255, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.70}
        size_hint: (0.23, 0.08)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "up"

<Statistics>:
    name: "stats"
    Image:
        source: "stats.jpg"
        allow_stretch: True
        
    MDRectangleFlatButton:
        text: "Statistics"
        font_size: 50
        theme_text_color: "Custom"
        text_color: 135/255,206/255,235/255, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.70}
        size_hint: (0.23, 0.08)
        on_release:
            root.run()
        
    
        
        
    MDFillRoundFlatButton:
        text: "Back"
        font_size: 20
        pos_hint: {'center_x':0.20, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "left"
            
            
<Toss>:
    name: "TossScreen"
    Image:
        source: "toss.jpg"
        allow_stretch: True
    
    MDLabel:
        id: abc
        text: ""
        halign: "center"
        font_style: "H4"
        pos_hint: {'center_x':0.5, 'center_y':0.80}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        
    MDRectangleFlatButton:
        id: LetsHaveToss
        disabled: False
        text: "Let's have a Toss"
        font_size: 30
        theme_text_color: "Custom"
        text_color: 135/255,206/255,235/255, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.90}
        size_hint: (0.23, 0.10)
        
        on_release:
            root.run()
    
    MDFillRoundFlatButton:
        text: "Back"
        font_size: 20
        pos_hint: {'center_x':0.20, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "right"
            
    
    MDRectangleFlatButton:
        id: oddButton
        pos_hint: {'center_x':0.60, 'center_y':0.70}
        size_hint: 0.12, 0.12
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.odd()
            
    MDRectangleFlatButton:
        id: evenButton
        pos_hint: {'center_x':0.40, 'center_y':0.70}
        size_hint: 0.12, 0.12
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.even()
            
    MDRectangleFlatButton:
        id: haveToss
        size_hint: 0.40, 0.03
        pos_hint: {'center_x':0.50, 'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        
        on_release:
            root.haveToss()
    
    MDLabel:
        id: toss1
        text: " "
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H5"
        halign: "center"
        pos_hint: {'center_x':0.50, 'center_y':0.59}
        
    MDLabel:
        id: tossPrint
        text: " "
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H5"
        halign: "center"
        size: .2,.05
        pos_hint: {'center_x':0.50, 'center_y':0.50}
       
    MDRectangleFlatButton:
        id: hand1
        text: "1"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.35, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.initiateToss1()
        
    MDRectangleFlatButton:
        id: hand2
        text: "2"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.50, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.initiateToss2()
            
            
    MDRectangleFlatButton:
        id: hand3
        text: "3"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.65, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.initiateToss3()
            
            
    MDRectangleFlatButton:
        id: hand4
        text: "4"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.35, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.initiateToss4()
            
    MDRectangleFlatButton:
        id: hand5
        text: "5"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.50, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.initiateToss5()
            
    MDRectangleFlatButton:
        id: hand6
        text: "6"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.65, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.initiateToss6()
            
            
    MDLabel:
        id: tossResult
        text: " "
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H5"
        halign: "center"
        size: .2,.05
        pos_hint: {'center_x':0.50, 'center_y':0.10}
        
        
    MDLabel:
        id: userSelection
        text: ""
        font_style: "H5"
        halign: "center"
        pos_hint: {'center_x':0.50, 'center_y':0.46}
        
    MDRectangleFlatButton:
        id: Continue
        text: " "
        pos_hint: {'center_x':0.50, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.ContinueTo()
        
<TossSelection>:
    name: "TossSelection"
    Image:
        source: "ball.jpg"
        allow_stretch: True
        
    MDFillRoundFlatButton:
        text: "Back"
        font_size: 20
        pos_hint: {'center_x':0.20, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "right"
        
    MDRectangleFlatButton:
        id: pressToContinue
        disabled: False
        text: "Press to choose Bating or Bowling."
        font_size: 30
        theme_text_color: "Custom"
        text_color: 135/255,206/255,235/255, 1
        line_color: 0, 0, 0, 1
        pos_hint: {'center_x':0.5, 'center_y':0.90}
        size_hint: (0.33, 0.10)
        
        on_release:
            root.run()
    
    MDLabel:
        id: printText
        text: " "
        font_style: "H3"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.80}
    
    MDRectangleFlatButton:
        id: batFirst
        text: " "
        pos_hint: {'center_x': 0.35, 'center_y': 0.70}
        size_hint: (0.25, 0.10)
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.userBatsFirst()

    MDRectangleFlatButton:
        id: bowlFirst
        text: " "
        pos_hint: {'center_x':0.65, 'center_y':0.70}
        size_hint: (0.25, 0.10)
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.userBowlsFirst()
            
        
<PlayGame>:
    name: "PlayGame"
    Image:
        source: "cricket2.jpg"
        allow_stretch: True
        
    MDFillRoundFlatButton:
        text: "Back"
        font_size: 20
        pos_hint: {'center_x':0.20, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "right"
            
    MDRectangleFlatButton:
        id: tossSelectionRun
        disabled: False
        text: "Press to continue"
        font_size: 30
        theme_text_color: "Custom"
        text_color: 135/255,206/255,235/255, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.95}
        size_hint: (0.25, 0.08)
        
        on_release:
            root.run()
       
    MDRectangleFlatButton:
        id: Hand1
        text: "1"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.35, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand1()
        
    MDRectangleFlatButton:
        id: Hand2
        text: "2"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.50, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand2()
            
            
    MDRectangleFlatButton:
        id: Hand3
        text: "3"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.65, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand3()

            
    MDRectangleFlatButton:
        id: Hand4
        text: "4"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.35, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand4()

            
    MDRectangleFlatButton:
        id: Hand5
        text: "5"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.50, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_colo: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand5()

            
    MDRectangleFlatButton:
        id: Hand6
        text: "6"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.65, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand6()

    MDLabel:
        id: userSelects
        text: ""
        font_style: "H5"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 0     
        
    MDLabel:
        id: printPlayerScore
        text: ""
        halign: "center"
        font_style: "H3"
        pos_hint: {"center_x":0.30, "center_y":0.65}
        
    MDLabel:
        id: printCompScore
        halign: "center"
        text: " "
        font_style: "H3"
        pos_hint: {"center_x":0.70, "center_y":0.65}
        
    
    MDLabel:
        id: printSelection
        text: " "
        font_style: "H5"
        halign: "center"
        pos_hint: {'center_x':0.50, 'center_y':0.88}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1     
   
    Image:
        id: handP
        pos_hint: {"center_x": 0.40, 'center_y': 0.75}
        size_hint: 0.12, 0.12
        opacity: 0
        
    Image:
        id: handC
        pos_hint: {"center_x": 0.60, 'center_y': 0.75}
        size_hint: 0.12, 0.12
        opacity: 0
    
<PlayGame2>:    
    name: "PlayGame2"
    Image:
        source: "cricket2.jpg"
        allow_stretch: True
        
    MDFillRoundFlatButton:
        text: "Back"
        font_size: 20
        pos_hint: {'center_x':0.20, 'center_y':0.05}
        size_hint: (0.10, 0.05)
        on_release:
            root.manager.current = 'Screen0'
            root.manager.transition.direction = "right"
            
    MDRectangleFlatButton:
        id: tossSelectionRun
        disabled: False
        text: "Press to continue"
        font_size: 30
        theme_text_color: "Custom"
        text_color: 135/255,206/255,235/255, 1
        line_color: 0, 0, 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.95}
        size_hint: (0.25, 0.08)
        
        on_release:
            root.run()
       
    MDLabel:
        id: printInnings
        halign: "center"
        font_style: "H5"
        text: ""
        pos_hint: {'center_x':0.5, 'center_y':0.85}
    
    
    MDRectangleFlatButton:
        id: Hand1
        text: "1"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.35, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand1()
        
    MDRectangleFlatButton:
        id: Hand2
        text: "2"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.50, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand2()
            
            
    MDRectangleFlatButton:
        id: Hand3
        text: "3"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.65, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand3()

            
    MDRectangleFlatButton:
        id: Hand4
        text: "4"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.35, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand4()

            
    MDRectangleFlatButton:
        id: Hand5
        text: "5"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.50, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_colo: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand5()

            
    MDRectangleFlatButton:
        id: Hand6
        text: "6"
        font_size: 0
        size_hint: 0.06, 0.12
        pos_hint: {'center_x':0.65, 'center_y':0.20}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0
        line_color: 0, 0, 0, 0
        disabled: True
        on_release:
            root.Hand6()

    MDLabel:
        id: userSelects
        text: ""
        font_style: "H5"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 0     
        
    MDLabel:
        id: printPlayerScore
        text: ""
        halign: "center"
        font_style: "H3"
        pos_hint: {"center_x":0.35, "center_y":0.65}
        
    MDLabel:
        id: printCompScore
        halign: "center"
        text: " "
        font_style: "H3"
        pos_hint: {"center_x":0.65, "center_y":0.65}
        
    
    MDLabel:
        id: printSelection
        text: " "
        font_style: "H5"
        halign: "center"
        pos_hint: {'center_x':0.50, 'center_y':0.88}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1     
   
    Image:
        id: handP
        pos_hint: {"center_x": 0.40, 'center_y': 0.75}
        size_hint: 0.12, 0.12
        opacity: 0
        
    Image:
        id: handC
        pos_hint: {"center_x": 0.60, 'center_y': 0.75}
        size_hint: 0.12, 0.12
        opacity: 0
        
    
    
    
    
    
'''
actionsInToss = '''
<EvenButton>:
    pos_hint: {'center_x':0.40, 'center_y':0.70}
    size_hint: 0.12, 0.12
    theme_text_color: "Custom"
    text_color: 0, 0, 0, 0
    line_color: 0, 0, 0, 0

        
    Image: 
        source: "Heads.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y
    
    
        
<EvenLabel>:
    text: "EVEN"
    halign: "center"
    font_style: "H6"
    pos_hint: {'center_x':0.40, 'center_y':0.62}
    

<OddButton>:
    pos_hint: {'center_x':0.60, 'center_y':0.70}
    size_hint: 0.12, 0.12
    theme_text_color: "Custom"
    text_color: 0, 0, 0, 0
    line_color: 0, 0, 0, 0
    
    Image: 
        source: "Tails.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y
        
    
        
<OddLabel>:
    text: "ODD"
    font_style: "H6"
    halign: "center"
    pos_hint: {'center_x':0.60, 'center_y':0.62}
    
<orLabel>:
    text: "OR"
    font_style: "H4"
    halign: "center"
    pos_hint: {'center_x':0.50, 'center_y':0.70}

<confirmButton>:
    text: "Press this to Confirm your selection and continue."
    font_style: "H5"
    halign: "center"
    size: .2,.05
    pos_hint: {'center_x':0.50, 'center_y':0.55}

<hand1>:
    halign: "center"
    
    pos_hint: {'center_x': 0.35, 'center_y': 0.35}
    Image:
        source: "finger1-removebg.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y
<hand2>:
    halign: "center"
    
    pos_hint: {'center_x': 0.50, 'center_y': 0.35}
    Image:
        source: "finger2-removebg.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y

<hand3>:
    halign: "center"
    
    pos_hint: {'center_x': 0.65, 'center_y': 0.35}
    Image:
        source: "finger3-removebg.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y
    
<hand4>:
    halign: "center"
    
    pos_hint: {'center_x': 0.35, 'center_y': 0.20}
    Image:
        source: "finger4-removebg.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y

<hand5>:
    halign: "center"
    
    pos_hint: {'center_x': 0.50, 'center_y': 0.20}
    Image:
        source: "finger5-removebg.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y

<hand6>:
    halign: "center"
    
    pos_hint: {'center_x': 0.65, 'center_y': 0.20}
    Image:
        source: "finger6-removebg.png"
        center_x: self.parent.center_x
        center_y: self.parent.center_y
        
<Continue>:
    text: "continue"
    font_style: "H6"
    halign: "center"
    pos_hint: {'center_x':0.50, 'center_y':0.05}
'''

actionsInTossSelection = '''

<BatFirst>:    
    halign: "center"
    pos_hint: {'center_x': 0.35, 'center_y': 0.70}
    Image:
        source: "batfirst.jpg"
        center_x: self.parent.center_x
        center_y: self.parent.center_y
        allow_stretch: True
        size_hint_y: None
        width: 300 
        
<BowlFirst>:
    halign: "center"
    pos_hint: {'center_x':0.65, 'center_y':0.70}
    Image:
        source: "bowlfirst.jpg"
        center_x: self.parent.center_x
        center_y: self.parent.center_y
        allow_stretch: True
        size_hint_y: None
        width: 300 


'''
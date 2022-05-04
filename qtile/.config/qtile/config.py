# pomcom@mailbox.org

from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

keys = [
   # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(),
            desc="Move window focus to other window"),

        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift", "control"], "h", lazy.layout.shuffle_left(),
            desc="Move window to the left"),
        Key([mod, "shift", "control"], "l", lazy.layout.shuffle_right(),
            desc="Move window to the right"),
        Key([mod, "shift", "control"], "j", lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([mod, "shift", "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(),
            desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(),
            desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(),
            desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        
        # move to group right and left
        Key([mod, "shift"], "l",
        lazy.screen.next_group(skip_empty=True),
        desc="Move to next active group"
        ),
        Key([mod, "shift"], "h",
        lazy.screen.prev_group(skip_empty=True),
        desc="Move to previous active group"
        ),

        Key([mod, "shift"], "c", lazy.screen.togglegroup()),

        Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),

        #shutdown qtile
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

        #Pulse Audio Controle
    
        Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),
        Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse sset Master 5%-")),
        Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse sset Master 5%+")),
        Key([], "XF86MonBrightnessUp", lazy.spawn('xbacklight -inc 10')),
        Key([], "XF86MonBrightnessDown", lazy.spawn('xbacklight -dec 10')),

        Key([mod], "space", lazy.spawn("rofi -show run")),
         # rofi window navigation
        Key([mod], "m", lazy.spawn("rofi -show")),
         # screenshot
         Key([mod], "s", lazy.spawn("spectacle")),
         # Screenlock
       #  Key([mod, "control"], "q", lazy.spawn("betterlockscreen -l")),
    
        # firefox dev edition
        Key([mod], "f", lazy.spawn("firefox-developer-edition")),

    ]




# Groups
group_setup = (
    (' ₁' , {  # fa-globe
        'layout': 'max',
        'matches': [Match(wm_class=('Firefox Developer Edition', 'Google-chrome'))],
    }),
    (' ₂', {  # fa-code
        'layout': 'max',
        'matches': [Match(wm_class=('',))],
    }),
    (' ₃', {}),  # fa-terminal
    (' ₄', {'layout': 'max'}),
    (' ₅', {
        'layout': 'max',
        'matches': [Match(wm_class=())],
    }),
    ('阮 ₆', {
        'layout': 'max',
        'matches': [Match(wm_class=('Steam',))],
    }),
    (' ₇', {}),
    (' ₈', {'layout': 'max', 'matches': [Match(wm_class=('VirtualBox',))]}),
    (' ₉', {
        'layout': 'max',
    }),
)


groups = []
for idx, (label, config) in enumerate(group_setup):
    hotkey = str(idx + 1)
    config.setdefault('layout', 'tile')
    groups.append(Group(label, **config))
    # mod + hotkey = switch to group
    keys.append(Key([mod], hotkey, lazy.group[label].toscreen()))

    # mod + shift + hotkey = move focused window to group
    keys.append(Key([mod, 'shift'], hotkey, lazy.window.togroup(label)))

#from libqtile.dgroups import simple_key_binder
#dgroups_key_binder = simple_key_binder("mod4")

def init_layout_theme():
    return {"margin":4,
            "border_width":3,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }
layout_theme = init_layout_theme()



layouts = [
        layout.Columns(**layout_theme),
        layout.Max(**layout_theme)
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        #layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
        # layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a")
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
        # layout.floating.Floating(),
    ]

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens   

widget_defaults = dict(
    font='MesloLGS NF',
    fontsize=14,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [   
                widget.Spacer(length=10),
                widget.GroupBox(borderwidth=4, inactive='969696', font='FiraCode Nerd Font', this_current_screen_border='eee8d5', this_screen_border='eee8d5', fontsize=20, highlight_method='line', highlight_color=['00000000','00000000'], disable_drag=True),
                widget.Spacer(length=10),
                widget.CurrentLayoutIcon(scale=0.7),
                widget.CurrentLayout(**widget_defaults),
                widget.Prompt(**widget_defaults),
                widget.Spacer(),
                #widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
               # widget.TextBox("pomcom", name="default"),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                    ),
                widget.Sep(
                    linewidth =1,
                    padding = 10,
                    ),
                widget.CPU(),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                    ),
                widget.Memory(
                       foreground = colors[2],
                       measure_mem = "G",
                       #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       ),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                    ),
                widget.Battery(
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                    ),
                widget.Systray(
                    backbround = colors[0],
                    padding = 5,
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                    ),
                widget.Clock(format='%d-%m %a %I:%M %p'),
                widget.Spacer(length=10),
            ],
            24, background="#000000AA", margin=[5, 8, 4, 5],
        ),
    ),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


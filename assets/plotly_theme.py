# -*- coding: utf-8 -*-
""" Template & Stylesheet for Plotly TopGun

Author: David J McNay
"""

import streamlit as st
import plotly.graph_objs as go
import plotly.io as pio


# https://swdevnotes.com/python/2020/plotly_customise_toolbar/
# https://plotly.com/python/configuration-options/
MODEBAR_CONFIG = {
    "displayModeBar": True,         # show mode bar
    "displaylogo": False,           # remove plotly logo
    'toImageButtonOptions': {
        'format': 'svg',            # one of png, svg, jpeg, webp
        'filename': 'plot',
        'scale': 1                  # Multiply title/legend/axis/canvas sizes by this factor
    },
    'modeBarButtonsToRemove': [
        'zoom2d', 'zoomIn2d', 'zoomOut2d',
        'toggleSpikelines',
        'pan2d',
        'select2d',
        'autoScale2d',
        'resetScale2d',             # just double click
        'hoverClosestCartesian',
        'hoverCompareCartesian',
    ],
    'modeBarButtonsToAdd': [
        'drawline',
        'drawopenpath',
        'eraseshape'],
}

STANLIB_CI = dict(

    # Highlight Colour - Only to be used on Dark Charts
    ElectricTeal='#90FBFE',

    # Primary Colours
    GreyWhite="#EDF0F8",
    LightGrey="#A6ADB5",
    DarkGrey="#777F88",
    DarkBlue="#2B3341",

    # Secondary Colours
    Danube="#4F89C7",
    Viking="#54C6D5",
    MediumRedViole="#CE3887",
    OceanGreen="#46BA7C",
    TanHide="#F68B4E",
    Deluge="#835DA7",
    Shocking="#E199C3",

    Froly='#F16474',
    MountainMeadow='#18A589',

    Bouquet='#BA7FB7',
    ShipCove="#677ABC",
    CeriseRed="#DB2D58",
    SeaPink="#EFABA5",
    Apple="#6DA548",
    Flamingo="#F04E3E",

    # That is the end of the new colours; use STANLIB old as overflow
    TealOld="#00A3AD",  #
    SkyOld="#00BBDC",  #
    RoyalOld="#0057B8",  #
    OrchidOld='#84329B',  #
    WineOld='#A20067',  #
    MonarchOld='#FC4C02',  #
    SunriseOld='#FF8200',  #
    SpringOld='#78BE20',  #
    AppleOld='#C4D600',  #
    RayOld='#F3E500',  #
    AegeanOld='#28334A',  #
    SlateOld='#A7A8AA',  #
    OliveOld='#584446',  #
    WalnutOld='#672E45',  #
    SaphireOld='#385E9D',  #
    GraphiteOld='#86647A',  #
    DoplhinOld='#A2B2C8',  #
    AzureOld='#4D5F80',  #
    AmberOld='#FED880',  #
    OysterOld='#CEB888',  #
)


def px_template(name='multi_strat',
                colourmap=list(STANLIB_CI.values())[4:],
                as_default=True):
    """ Setup Default Plotly Template - for use with Plotly Express

        Just run function in notebook to make template available

    References:
        https://plotly.com/python/templates/
        https://www.kite.com/python/docs/plotly.graph_objs.Layout.modebar
    """

    fig = go.Figure(
        layout=dict(
            title_font={'family': 'Astoria'},  # Broken in Plotly back end... raised ticket
            font={
                'family': 'Astoria',  # Garamond (DM preference) | Astoria
                'size': 12,
                'color': '#2B3341',
            },
            plot_bgcolor='white',
            paper_bgcolor='white',
            colorway=colourmap,
            showlegend=True,
            legend={'orientation': 'v'},
            margin={'l': 75, 'r': 50, 'b': 50, 't': 50},
            xaxis={
                'anchor': 'y1',
                'showline': True, 'linecolor': 'gray',
                'zeroline': True, 'zerolinewidth': 1, 'zerolinecolor': 'whitesmoke',
                'showgrid': True, 'gridcolor': 'whitesmoke',
            },
            yaxis={
                'anchor': 'x1',
                'hoverformat': '.2f',
                'tickformat': '.1f',
                'showline': True, 'linecolor': 'gray',
                'zeroline': True, 'zerolinewidth': 1, 'zerolinecolor': 'whitesmoke',
                'showgrid': True, 'gridcolor': 'whitesmoke'
            },
            modebar={
                'bgcolor': 'rgba(255 ,255 ,255 , 0)',  # transparent
                'color': 'whitesmoke',
                'activecolor': STANLIB_CI['DarkBlue'],
            },
        ))

    # set template in pio - remember only last for the session
    pio.templates[name] = pio.to_templated(fig).layout.template

    # can specify this as the default template for a session
    # just means we can skip the template='multi_strat' line
    if as_default:
        pio.templates.default = name

    return

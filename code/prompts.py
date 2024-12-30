example_data_schema_str = """
{"number_rows": 1461,
 "field": [{"name": "date",
   "type": "datetime",
   "unique": 1461,
   "entropy": 7287},
  {"name": "precipitation",
   "type": "number",
   "unique": 111,
   "entropy": 2422,
   "min": 0,
   "max": 55,
   "std": 6},
  {"name": "temp_max",
   "type": "number",
   "unique": 67,
   "entropy": 3934,
   "min": -1,
   "max": 35,
   "std": 7},
  {"name": "temp_min",
   "type": "number",
   "unique": 55,
   "entropy": 3596,
   "min": -7,
   "max": 18,
   "std": 5},
  {"name": "wind",
   "type": "number",
   "unique": 79,
   "entropy": 3950,
   "min": 0,
   "max": 9,
   "std": 1},
  {"name": "weather",
   "type": "string",
   "unique": 5,
   "entropy": 1201,
   "freq": 714}]}
"""

tick_plot = """
# Tick Plot
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "tick",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear"
        }
      ]
    }
  ]
}
"""

tick_plot_log = """
# Tick Plot with a Log Scale
{
  "number_rows": 1456,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "tick",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "log"
        }
      ]
    }
  ]
}
"""

bar_chart = """
# Bar Chart
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "coordinates": "cartesian",
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "field": "weather"
            },
            {
              "channel": "y",
              "field": "temp_max",
              "aggregate": "mean"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "ordinal"
        },
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        }
      ]
    }
  ]
}
"""

radial_chart = """
# Radial Chart
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "coordinates": "polar",
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "field": "weather"
            },
            {
              "channel": "y",
              "field": "temp_max",
              "aggregate": "mean"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "ordinal"
        },
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        }
      ]
    }
  ]
}
"""

histogram = """
# Histogram
{
  "number_rows": 1461,
  "field": [
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "field": "weather"
            },
            {
              "channel": "y",
              "aggregate": "count"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "ordinal"
        },
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        }
      ]
    }
  ]
}
"""

binned_histogram = """
# Binned Histogram
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max",
              "binning": 10
            },
            {
              "channel": "y",
              "aggregate": "count"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear"
        },
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        }
      ]
    }
  ]
}
"""


scatter_plot = """
# Scatter Plot
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "wind",
      "type": "number",
      "__id__": "wind"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "point",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max"
            },
            {
              "channel": "y",
              "field": "wind"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear"
        },
        {
          "channel": "y",
          "type": "linear"
        }
      ]
    }
  ]
}
"""

scatter_plot_color = """
# Scatter Plot with Color Encoding
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "wind",
      "type": "number",
      "__id__": "wind"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "point",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max"
            },
            {
              "channel": "y",
              "field": "wind"
            },
            {
              "channel": "color",
              "field": "weather"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear"
        },
        {
          "channel": "y",
          "type": "linear"
        },
        {
          "channel": "color",
          "type": "categorical"
        }
      ]
    }
  ]
}
"""

bubble_chart = """
# Bubble Chart
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "wind",
      "type": "number",
      "__id__": "wind"
    },
    {
      "name": "precipitation",
      "type": "number",
      "__id__": "precipitation"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "point",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max"
            },
            {
              "channel": "y",
              "field": "wind"
            },
            {
              "channel": "size",
              "field": "precipitation"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear"
        },
        {
          "channel": "y",
          "type": "linear"
        },
        {
          "channel": "size",
          "type": "linear"
        }
      ]
    }
  ]
}
"""

pie_chart = """
# Pie Chart
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "coordinates": "polar",
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "y",
              "aggregate": "count",
              "stack": "zero"
            },
            {
              "channel": "color",
              "field": "weather"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        },
        {
          "channel": "color",
          "type": "categorical"
        }
      ]
    }
  ]
}
"""

stacked_bar_chart = """
# Stacked Bar Chart
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max",
              "binning": 10
            },
            {
              "channel": "y",
              "aggregate": "count",
              "stack": "zero"
            },
            {
              "channel": "color",
              "field": "weather"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear"
        },
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        },
        {
          "channel": "color",
          "type": "categorical"
        }
      ]
    }
  ]
}
"""

normolized_stacked_bar_chart = """
# Normalized Stacked Bar Chart
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "aggregate": "count",
              "stack": "normalize"
            },
            {
              "channel": "y",
              "field": "temp_max",
              "binning": 10
            },
            {
              "channel": "color",
              "field": "weather"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear",
          "zero": "true"
        },
        {
          "channel": "y",
          "type": "linear"
        },
        {
          "channel": "color",
          "type": "categorical"
        }
      ]
    }
  ]
}
"""

bar_with_tick = """
# Bar Chart with Tick Plot
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "aggregate": "mean",
              "field": "temp_max"
            }
          ]
        },
        {
          "type": "tick",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear",
          "zero": "true"
        }
      ]
    }
  ]
}
"""

facet_scatter_plot_column = """
# Facet Scatter Plot by Column
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "wind",
      "type": "number",
      "__id__": "wind"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "point",
          "encoding": [
            {
              "channel": "x",
              "field": "temp_max"
            },
            {
              "channel": "y",
              "field": "wind"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "linear"
        },
        {
          "channel": "y",
          "type": "linear"
        }
      ],
      "facet": [
        {
          "channel": "col",
          "field": "weather"
        }
      ]
    }
  ]
}
"""


facet_scatter_plot_binned = """
# Facet Scatter Plot with Binned Column
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "wind",
      "type": "number",
      "__id__": "wind"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "point",
          "encoding": [
            {
              "channel": "x",
              "field": "weather"
            },
            {
              "channel": "y",
              "field": "wind"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "ordinal"
        },
        {
          "channel": "y",
          "type": "linear"
        }
      ],
      "facet": [
        {
          "channel": "col",
          "field": "temp_max",
          "binning": 10
        }
      ]
    }
  ]
}
"""

tick_plot_histogram = """
# Tick Plot with Histogram
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "tick",
          "encoding": [
            {
              "channel": "y",
              "field": "temp_max"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        }
      ]
    },
    {
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "x",
              "field": "weather"
            },
            {
              "channel": "y",
              "aggregate": "count"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "ordinal"
        },
        {
          "channel": "y",
          "type": "linear",
          "zero": "true"
        }
      ]
    }
  ]
}
"""

tick_plot_histogram_y_scale = """
# Tick Plot with Histogram and Y Scale
{
  "number_rows": 1461,
  "field": [
    {
      "name": "temp_max",
      "type": "number",
      "__id__": "temp_max"
    },
    {
      "name": "weather",
      "type": "string",
      "__id__": "weather"
    }
  ],
  "view": [
    {
      "mark": [
        {
          "type": "tick",
          "encoding": [
            {
              "channel": "y",
              "field": "temp_max"
            }
          ]
        }
      ]
    },
    {
      "mark": [
        {
          "type": "bar",
          "encoding": [
            {
              "channel": "y",
              "field": "temp_max",
              "aggregate": "mean"
            },
            {
              "channel": "x",
              "field": "weather"
            }
          ]
        }
      ],
      "scale": [
        {
          "channel": "x",
          "type": "ordinal"
        }
      ]
    }
  ],
  "scale": [
    {
      "channel": "y",
      "type": "linear",
      "zero": "true"
    }
  ]
}
"""

example_plot_schemas = [
    tick_plot,
    tick_plot_log,
    bar_chart,
    radial_chart,
    histogram,
    binned_histogram,
    scatter_plot,
    scatter_plot_color,
    bubble_chart,
    pie_chart,
    stacked_bar_chart,
    normolized_stacked_bar_chart,
    bar_with_tick,
    facet_scatter_plot_column,
    facet_scatter_plot_binned,
    tick_plot_histogram,
    tick_plot_histogram_y_scale,
]

example_plot_schemas_str = "\n".join(example_plot_schemas)
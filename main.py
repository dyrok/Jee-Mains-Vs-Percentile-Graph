import matplotlib.pyplot as plt
import mplcursors

# Define JEE Main Marks, Percentiles, and Ranks
jee_marks = [i for i in range(10, 300, 10)]
jee_percentile = [
    (100, 99.99989145),
    (99.994681, 99.997394),
    (99.990990, 99.994029),
    (99.977205, 99.988819),
    (99.960163, 99.975034),
    (99.934980, 99.956364),
    (99.901113, 99.928901),
    (99.851616, 99.893732),
    (99.795063, 99.845212),
    (99.710831, 99.782472),
    (99.597399, 99.688579),
    (99.456939, 99.573193),
    (99.272084, 99.431214),
    (99.028614, 99.239737),
    (98.732389, 98.990296),
    (98.317414, 98.666935),
    (97.811260, 98.254132),
    (97.142937, 97.685672),
    (96.204550, 96.978272),
    (94.998594, 96.064850),
    (93.471231, 94.749479),
    (91.072128, 93.152971),
    (87.512225, 90.702200),
    (82.016062, 86.907944),
    (73.287808, 80.982153),
    (58.151490, 71.302052)
]

jee_rank = [
    (1, 20),
    (80, 24),
    (83, 55),
    (210, 85),
    (367, 215),
    (599, 375),
    (911, 610),
    (1367, 920),
    (1888, 1375),
    (2664, 1900),
    (3710, 2700),
    (5003, 3800),
    (6706, 5100),
    (8949, 6800),
    (11678, 9000),
    (15501, 11800),
    (20164, 15700),
    (26321, 20500),
    (34966, 26500),
    (46076, 35000),
    (60147, 46500),
    (82249, 61000),
    (115045, 83000),
    (165679, 117000),
    (246089, 166000),
    (385534, 26438)
]

# Extracting JEE Main Percentiles and Ranks
x = [percentile[0] for percentile in jee_percentile]
y = jee_marks[:len(x)][::-1]
ranks = [rank[0] for rank in jee_rank]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, marker='o', linestyle='-')
ax.set_title('JEE Main Marks vs Percentile')
ax.set_xlabel('JEE Main Percentile')
ax.set_ylabel('JEE Main Marks')
ax.grid(True)
ax.set_ylim(0, max(jee_marks))  # Set y-axis limits from 0 to the maximum JEE Main mark
ax.invert_yaxis()  # Invert y-axis to have higher marks at the top

# Annotate ranks on hover
mplcursors.cursor(hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(f"Rank: {ranks[int(sel.target.index)]}")
)

plt.show()

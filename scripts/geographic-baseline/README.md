# How to Pre-compute Geographic Baselines

To generate baselines for the geographic advantage metric, you first need to

* Extract fully connected adjancency graphs, and
* Extract data from geojson files for all available elections

Those steps are described in the README files in the `scripts/graphs` and `scripts/data` directories.

## Find neighborhoods

With those done, you find "neighborhoods" for each state and chamber combination.
This is a long-running script! It take many hours on an M4 MacBook.

```bash
scripts/geographic-baseline/FIND-NEIGHORHOODS.sh
```

Because they are quite large, neighborhoods are stored in a highly compressed format.
You can confirm that they "round trip" correctly, you can run this script.

```bash
scripts/geographic-baseline/CHECK-NEIGHBORHOODS.sh
```

While geographic baselines (computed below) need to be updated as new elections are available,
the neighborhoods only need to be done once per census cycle--they only depend on total population.

## Calculate baselines

Once you have computed neighborhoods, you can calculate baselines for each state and chamber combination.

```bash
scripts/geographic-baseline/ONCE.sh
```

Other one-time preprocessing could be added to this script.

You can produce a report of the geographic baselines, using this script.

```bash
scripts/geographic-baseline/report_baselines.py
```

Once geographic baselines are computed, you can use them in scoring.
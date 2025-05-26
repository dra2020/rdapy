# How to Pre-compute Geographic Baselines

To generate baselines for the geographic advantage metric, 
you first need to:

* Extract fully connected adjancency graphs from the DRA geojsons, and
* Extract input data from DRA geojson files for all available elections

Those steps are described in the README files in the `scripts/graphs` and `scripts/data` directories, respectively.

## Find neighborhoods

With those done, you first find "neighborhoods" for each state and chamber combination.
This only need to be found once per census cycle: neighborhods only depend on total population and precinct adjacency.
This is a very long-running script--it takes nearly 10 hours on an M4 MacBook!--so the resulting files should be saved.

```bash
scripts/geographic-baseline/FIND-NEIGHORHOODS.sh
```

Because they are quite large, neighborhoods are stored in a highly compressed format.
You can confirm that they "round trip" correctly, you can run this script.

```bash
scripts/geographic-baseline/CHECK-NEIGHBORHOODS.sh
```

## Calculate baselines

Once you have computed neighborhoods, you can calculate baselines for each state and chamber combination.

```bash
scripts/geographic-baseline/ONCE.sh
```

The geographic baselines for a state need to be updated every time a new election is available for that state.
To do that, use the appropriate lines in `scripts/geographic-baseline/ONCE.sh`.
Computing the baselines is relatively fast, but it only needs to be done once for every unique set of elections
for a state, so, again, these files should be saved and updated as needed.

Right now, the only thing we precompute is geographic baselines.
Other one-time preprocessing could, however, be added to this script.

You can produce a report of the geographic baselines, using this script.

```bash
scripts/geographic-baseline/report_baselines.py
```

Once geographic baselines are computed, you can use them in scoring.
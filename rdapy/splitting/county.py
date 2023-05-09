#!/usr/bin/env python3

"""
COUNTY-DISTRICT SPLITTING -- building on Moon Duchin's work
"""

import math
import copy


def split_score(split: list[float]) -> float:
    """Moon Duchin's raw split score"""

    if len(split) > 0:
        return sum(map(math.sqrt, split))
    else:
        return 1.0


### HELPERS ###

# NOTE - The county-district splits and the county & district totals may all,
# in general, be fractional/decimal numbers as opposed to integers, due to
# dissaggregation & re-aggregation. Hence, comparisons need to approximate
# equality.


def county_totals(CxD: list[list[float]]) -> list[float]:
    """Total population of each county (column) in the CxD matrix"""

    nC: int = len(CxD[0])
    nD: int = len(CxD)
    totals: list[float] = [0.0] * nC

    for j in range(nC):
        for i in range(nD):
            totals[j] += CxD[i][j]

    return totals


def district_totals(CxD: list[list[float]]) -> list[float]:
    """Total population of each district (row) in the CxD matrix"""

    nC: int = len(CxD[0])
    nD: int = len(CxD)
    totals: list[float] = [0.0] * nD

    for j in range(nC):
        for i in range(nD):
            totals[i] += CxD[i][j]

    return totals


def reduceCSplits(CxD: list[list[float]], dTotals: list[float]) -> list[list[float]]:
    """Consolidate *whole districts* (w/in one county) UP into dummy district 0, county by county."""

    # Create the reduced template
    CxDreducedC: list[list[float]] = copy.deepcopy(CxD)
    nC: int = len(CxDreducedC[0])
    vRow: list[float] = [0.0] * nC
    CxDreducedC.insert(0, vRow)
    nD: int = len(CxDreducedC)

    for j in range(nC):
        # Skip the virtual district 0
        for i in range(1, nD):
            split_total: float = CxDreducedC[i][j]

            if split_total > 0:
                if math.isclose(split_total, dTotals[i - 1], abs_tol=1e-6):
                    CxDreducedC[0][j] += split_total
                    CxDreducedC[i][j] = 0

    return CxDreducedC


"""
// Consolidate *whole counties* (w/in one district) LEFT into the dummy county 0,
//   district by district.
export function reduceDSplits(CxD: T.CxD, countyTotals: number[]): number[][]
{
  // Create the reduced template
  let CxDreducedD: number[][] = U.deepCopy(CxD);
  CxDreducedD.map(row => row.unshift(0));
  const nC = CxDreducedD[0].length;
  const nD = CxDreducedD.length;

  for (let i = 0; i < nD; i++)
  {
    // Skip the virtual county 0
    for (let j = 1; j < nC; j++)
    {
      let split_total = CxDreducedD[i][j];

      if (split_total > 0)
      {
        if (U.areRoughlyEqual(split_total, countyTotals[j - 1], U.EQUAL_TOLERANCE))
        {
          CxDreducedD[i][0] += split_total;
          CxDreducedD[i][j] = 0;
        }
      }
    }
  }

  return CxDreducedD;
}

"""

# LIMIT WHAT GETS EXPORTED.

__all__ = ["split_score", "county_totals", "district_totals", "reduceCSplits"]

### END ###

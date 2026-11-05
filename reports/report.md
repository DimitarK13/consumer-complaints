# Electricity Demand and Pricing

## 1. Project Overview

This project explores consumer complaints about financial products and services in the United States using the [Consumer Complaints Database](https://www.kaggle.com/datasets/sebastienverpile/consumercomplaintsdata) dataset.

The analysis focuses on identifying complaint patterns, understanding how complaint volumes evolve over time, and exploring the factors associated with consumer disputes and company response outcomes.

## 2. Problem Statement

This project aims to explore patterns in US consumer financial complaints to identify the products and issues most frequently associated with complaints, examine changes in complaint volumes over time, and investigate differences in company response outcomes across various factors.

## 3. Objectives

- Identify which financial products and services generate the highest number of consumer complaints.
- Analyze complaint volume trends over time and identify notable changes.
- Examine which complaint issues have the highest proportion of disputed responses.
- Investigate which factors are associated with companies providing timely responses.
- Compare complaint patterns across submission channels and geographical regions.

## 4. Research Questions

- Which financial products generate the most complaints?
- How have complaint volumes changed over time?
- Which issues have the highest share of disputed complaints?
- Which factors are associated with timely company responses?
- Are there differences by submission channel or region?

## 5. Hypotheses

- The number of complaints has generally increased over time.

## 6. Data Quality Assessment

The consumer_disputed column contains approximately 14% missing values. This is not random, as the CFPB discontinued its consumer dispute option in April 2017.

This column indicates whether a consumer disputed the company's response to their complaint (Yes or No).

Instead of removing rows with missing values, they will be preserved as another category - 'Not available'.

Performance on Data Slices
This section reports how the model performs across demographic slices in the Adult Census dataset.
Performance is summarized using Precision, Recall, and F1-score, computed for each subgroup within key categorical features including workclass, education, marital-status, occupation, relationship, race, sex, and native-country.

Overall Observations
    • Performance varies significantly across subgroups.
    • Slices with large sample sizes (e.g., Private workclass, United-States, HS-grad) show stable and reliable scores.
    • Slices with very small sample sizes (e.g., Cambodia, Hungary, Yugoslavia, Priv-house-serv, Armed-Forces) often achieve perfect precision/recall/F1, but these values are not statistically reliable.
    • Some slices exhibit very poor performance, especially those with F1 = 0.0, indicating the model fails to identify positive cases in those groups.

1. Workclass Slices
    • The model performs best for:
        ○ Federal-gov (F1 = 0.79)
        ○ Self-emp-inc (F1 = 0.77)
        ○ State-gov (F1 = 0.70)
    • Lower-performing slices include:
        ○ Self-emp-not-inc (F1 = 0.58)
        ○ Unknown / “?” (F1 = 0.50)
    • Without-pay has F1 = 1.0 but with only 4 samples → not reliable.

2. Education Slices
    • Strong performance for:
        ○ Doctorate (F1 = 0.88)
        ○ Prof-school (F1 = 0.88)
        ○ Masters (F1 = 0.84)
        ○ Bachelors (F1 = 0.74)
    • Very poor performance for:
        ○ 7th–8th grade (F1 = 0.00)
        ○ 10th (F1 = 0.23)
        ○ 11th (F1 = 0.43)
    • Perfect F1 for extremely small groups:
        ○ 1st–4th, Preschool → not reliable.

3. Marital Status Slices
    • High F1 for:
        ○ Married-civ-spouse (F1 = 0.71)
    • Lower-performing groups:
        ○ Never-married (F1 = 0.56)
        ○ Divorced (F1 = 0.49)
    • Extremely poor or zero recall:
        ○ Married-AF-spouse (F1 = 0.00; only 4 samples)

4. Occupation Slices
    • Strong slices:
        ○ Exec-managerial (F1 = 0.77)
        ○ Prof-specialty (F1 = 0.78)
    • Weak slices:
        ○ Farming-fishing (F1 = 0.31)
        ○ Other-service (F1 = 0.32)
        ○ Handlers-cleaners (F1 = 0.42)
    • Many small categories (e.g., Armed-Forces, Priv-house-serv) show perfect F1 but with < 5 samples.

5. Relationship Slices
    • Strong performers:
        ○ Husband (F1 = 0.71)
        ○ Wife (F1 = 0.69)
    • Weak performers:
        ○ Own-child (F1 = 0.30)
        ○ Unmarried (F1 = 0.41)
    • Perfect F1 for Other-relative but recall = 0.375 indicates imbalance.

6. Race Slices
    • Strong performance:
        ○ Asian-Pac-Islander (F1 = 0.75)
        ○ Other (F1 = 0.80)
    • Weaker performance:
        ○ Amer-Indian-Eskimo (F1 = 0.55)
        ○ Black (F1 = 0.66)
    • Largest group (White) shows stable performance with F1 = 0.68.

7. Sex Slices
    • Male and Female slices show relatively close performance:
        ○ Male F1 = 0.70
        ○ Female F1 = 0.60
This indicates a moderate difference in performance by gender, with better recall for males.

8. Native Country Slices
    • Very inconsistent due to extreme class imbalance.
    • Large slice:
        ○ United-States (F1 = 0.68) → reliable
    • Many small slices show F1 = 1.0 due to having only 2–5 examples → not reliable.
    • Extremely low performance:
        ○ Greece (F1 = 0.00)
        ○ Iran (F1 = 0.25)
        ○ Hong (F1 = 0.66)
        ○ South (F1 = 0.40)
This reflects the model’s inability to learn meaningful patterns for underrepresented groups.

Summary of Fairness and Bias Considerations
    • The model demonstrates unequal performance across demographic subgroups, especially where sample sizes are small.
    • Several groups with F1 = 0.00 indicate complete failure to detect positive cases for those slices.
    • Groups with very high scores but very small support may give the false impression of strong performance.
    • Additional data balancing, oversampling, or fairness constraints may be required to ensure equitable performance across groups.

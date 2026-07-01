import great_expectations as gx
import pandas as pd

# Charger les données
df = pd.read_csv("data/transactions.csv")

# Créer un contexte GE
context = gx.get_context()

# Créer une datasource à partir du DataFrame
data_source = context.data_sources.add_pandas("transactions_source")
data_asset = data_source.add_dataframe_asset("transactions")
batch_definition = data_asset.add_batch_definition_whole_dataframe("batch")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

# Créer une suite d'expectations
suite = context.suites.add(gx.ExpectationSuite(name="transactions_suite"))

# Définir les expectations
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="id_transaction"))
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="montant"))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(column="montant", min_value=-1000, max_value=10000))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeInSet(column="statut", value_set=["validé", "en attente"]))

# Valider
validation_definition = context.validation_definitions.add(
    gx.ValidationDefinition(name="transactions_validation", data=batch_definition, suite=suite)
)
results = validation_definition.run(batch_parameters={"dataframe": df})
print(results)
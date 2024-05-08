from datacatalogtordf import Catalog, Dataset, Distribution, Agent, Contact


def main():
    organization = Agent(
        "https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789"
    )
    organization.name = {"nb": "Eksempeldirektorat", "en": "Example agency"}

    contact = Contact(
        "https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789"
    )
    contact.email = "example@example.org"

    catalog = create_catalog(
        identifier="http://data.norge.no/examplecatalog/123",
        title={"nb": "Eksempelkatalog"},
        description={"nb": "Dette er en eksempel-katalog"},
        publisher=organization,
        contactpoint=contact,
    )

    dataset1 = create_dataset(
        identifier="http://data.norge.no/exampledataset/123",
        title={"nb": "Eksempeldatasett 1"},
        description={"nb": "Dette er et eksempel-datasett"},
        publisher=organization,
        theme="http://publications.europa.eu/resource/authority/data-theme/EDUC",
    )

    dataset2 = create_dataset(
        identifier="http://data.norge.no/exampledataset/456",
        title={"nb": "Eksempeldatasett 2"},
        description={"nb": "Dette er et annet eksempel-datasett med en distribusjon"},
        publisher=organization,
        theme="http://publications.europa.eu/resource/authority/data-theme/GOVE",
    )
    dataset2.distributions = [
        create_distribution(
            "http://data.norge.no/exampledistribution/111",
            access_url="https://example.org/page/with_information/on/how_to/access/data",
        )
    ]

    catalog.datasets = [dataset1, dataset2]

    print(catalog.to_rdf(format="turtle").decode("utf-8"))


def create_catalog(identifier, title, description, publisher, contactpoint):
    catalog = Catalog(identifier=identifier)
    catalog.dct_identifier = identifier
    catalog.title = title
    catalog.description = description
    catalog.publisher = publisher
    catalog.contactpoint = contactpoint
    return catalog


def create_dataset(
    identifier,
    title,
    description,
    publisher,
    theme,
):
    dataset = Dataset(identifier=identifier)
    dataset.dct_identifier = identifier
    dataset.title = title
    dataset.description = description
    dataset.publisher = publisher
    dataset.theme = [theme]
    return dataset


def create_distribution(
    identifier,
    access_url,
):
    distribution = Distribution(identifier=identifier)
    distribution.access_URL = access_url
    return distribution


if __name__ == "__main__":
    main()

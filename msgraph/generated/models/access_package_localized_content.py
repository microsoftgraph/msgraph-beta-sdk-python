from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_localized_text import AccessPackageLocalizedText

@dataclass
class AccessPackageLocalizedContent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The fallback string, which is used when a requested localization isn't available. Required.
    default_text: Optional[str] = None
    # Content represented in a format for a specific locale.
    localized_texts: Optional[List[AccessPackageLocalizedText]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageLocalizedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageLocalizedContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageLocalizedContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_localized_text import AccessPackageLocalizedText

        from .access_package_localized_text import AccessPackageLocalizedText

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultText": lambda n : setattr(self, 'default_text', n.get_str_value()),
            "localizedTexts": lambda n : setattr(self, 'localized_texts', n.get_collection_of_object_values(AccessPackageLocalizedText)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("defaultText", self.default_text)
        writer.write_collection_of_object_values("localizedTexts", self.localized_texts)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


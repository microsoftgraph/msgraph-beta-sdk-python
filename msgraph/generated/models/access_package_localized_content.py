from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_localized_text = lazy_import('msgraph.generated.models.access_package_localized_text')

class AccessPackageLocalizedContent(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageLocalizedContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The fallback string, which is used when a requested localization is not available. Required.
        self._default_text: Optional[str] = None
        # Content represented in a format for a specific locale.
        self._localized_texts: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageLocalizedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageLocalizedContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageLocalizedContent()
    
    @property
    def default_text(self,) -> Optional[str]:
        """
        Gets the defaultText property value. The fallback string, which is used when a requested localization is not available. Required.
        Returns: Optional[str]
        """
        return self._default_text
    
    @default_text.setter
    def default_text(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultText property value. The fallback string, which is used when a requested localization is not available. Required.
        Args:
            value: Value to set for the defaultText property.
        """
        self._default_text = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_text": lambda n : setattr(self, 'default_text', n.get_str_value()),
            "localized_texts": lambda n : setattr(self, 'localized_texts', n.get_collection_of_object_values(access_package_localized_text.AccessPackageLocalizedText)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def localized_texts(self,) -> Optional[List[access_package_localized_text.AccessPackageLocalizedText]]:
        """
        Gets the localizedTexts property value. Content represented in a format for a specific locale.
        Returns: Optional[List[access_package_localized_text.AccessPackageLocalizedText]]
        """
        return self._localized_texts
    
    @localized_texts.setter
    def localized_texts(self,value: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None) -> None:
        """
        Sets the localizedTexts property value. Content represented in a format for a specific locale.
        Args:
            value: Value to set for the localizedTexts property.
        """
        self._localized_texts = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("defaultText", self.default_text)
        writer.write_collection_of_object_values("localizedTexts", self.localized_texts)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


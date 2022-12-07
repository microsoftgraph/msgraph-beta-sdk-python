from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_localized_content = lazy_import('msgraph.generated.models.access_package_localized_content')

class AccessPackageAnswerChoice(AdditionalDataHolder, Parsable):
    @property
    def actual_value(self,) -> Optional[str]:
        """
        Gets the actualValue property value. The actual value of the selected choice. This is typically a string value which is understandable by applications. Required.
        Returns: Optional[str]
        """
        return self._actual_value
    
    @actual_value.setter
    def actual_value(self,value: Optional[str] = None) -> None:
        """
        Sets the actualValue property value. The actual value of the selected choice. This is typically a string value which is understandable by applications. Required.
        Args:
            value: Value to set for the actualValue property.
        """
        self._actual_value = value
    
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
        Instantiates a new accessPackageAnswerChoice and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The actual value of the selected choice. This is typically a string value which is understandable by applications. Required.
        self._actual_value: Optional[str] = None
        # The localized display values shown to the requestor and approvers. Required.
        self._display_value: Optional[access_package_localized_content.AccessPackageLocalizedContent] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAnswerChoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAnswerChoice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAnswerChoice()
    
    @property
    def display_value(self,) -> Optional[access_package_localized_content.AccessPackageLocalizedContent]:
        """
        Gets the displayValue property value. The localized display values shown to the requestor and approvers. Required.
        Returns: Optional[access_package_localized_content.AccessPackageLocalizedContent]
        """
        return self._display_value
    
    @display_value.setter
    def display_value(self,value: Optional[access_package_localized_content.AccessPackageLocalizedContent] = None) -> None:
        """
        Sets the displayValue property value. The localized display values shown to the requestor and approvers. Required.
        Args:
            value: Value to set for the displayValue property.
        """
        self._display_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "actual_value": lambda n : setattr(self, 'actual_value', n.get_str_value()),
            "display_value": lambda n : setattr(self, 'display_value', n.get_object_value(access_package_localized_content.AccessPackageLocalizedContent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
        writer.write_str_value("actualValue", self.actual_value)
        writer.write_object_value("displayValue", self.display_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


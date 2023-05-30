from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_attribute_collection_page_view_configuration

class AuthenticationAttributeCollectionPage(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationAttributeCollectionPage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The customStringsFileId property
        self._custom_strings_file_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A collection of displays of the attribute collection page.
        self._views: Optional[List[authentication_attribute_collection_page_view_configuration.AuthenticationAttributeCollectionPageViewConfiguration]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationAttributeCollectionPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAttributeCollectionPage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationAttributeCollectionPage()
    
    @property
    def custom_strings_file_id(self,) -> Optional[str]:
        """
        Gets the customStringsFileId property value. The customStringsFileId property
        Returns: Optional[str]
        """
        return self._custom_strings_file_id
    
    @custom_strings_file_id.setter
    def custom_strings_file_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customStringsFileId property value. The customStringsFileId property
        Args:
            value: Value to set for the custom_strings_file_id property.
        """
        self._custom_strings_file_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_attribute_collection_page_view_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "customStringsFileId": lambda n : setattr(self, 'custom_strings_file_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "views": lambda n : setattr(self, 'views', n.get_collection_of_object_values(authentication_attribute_collection_page_view_configuration.AuthenticationAttributeCollectionPageViewConfiguration)),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("customStringsFileId", self.custom_strings_file_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("views", self.views)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def views(self,) -> Optional[List[authentication_attribute_collection_page_view_configuration.AuthenticationAttributeCollectionPageViewConfiguration]]:
        """
        Gets the views property value. A collection of displays of the attribute collection page.
        Returns: Optional[List[authentication_attribute_collection_page_view_configuration.AuthenticationAttributeCollectionPageViewConfiguration]]
        """
        return self._views
    
    @views.setter
    def views(self,value: Optional[List[authentication_attribute_collection_page_view_configuration.AuthenticationAttributeCollectionPageViewConfiguration]] = None) -> None:
        """
        Sets the views property value. A collection of displays of the attribute collection page.
        Args:
            value: Value to set for the views property.
        """
        self._views = value
    


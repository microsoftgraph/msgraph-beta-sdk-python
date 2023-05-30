from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_attribute_collection_input_configuration

class AuthenticationAttributeCollectionPageViewConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationAttributeCollectionPageViewConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The description of the page.
        self._description: Optional[str] = None
        # The display configuration of attributes being collected on the attribute collection page.
        self._inputs: Optional[List[authentication_attribute_collection_input_configuration.AuthenticationAttributeCollectionInputConfiguration]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The title of the attribute collection page.
        self._title: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationAttributeCollectionPageViewConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAttributeCollectionPageViewConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationAttributeCollectionPageViewConfiguration()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the page.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the page.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_attribute_collection_input_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "inputs": lambda n : setattr(self, 'inputs', n.get_collection_of_object_values(authentication_attribute_collection_input_configuration.AuthenticationAttributeCollectionInputConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        return fields
    
    @property
    def inputs(self,) -> Optional[List[authentication_attribute_collection_input_configuration.AuthenticationAttributeCollectionInputConfiguration]]:
        """
        Gets the inputs property value. The display configuration of attributes being collected on the attribute collection page.
        Returns: Optional[List[authentication_attribute_collection_input_configuration.AuthenticationAttributeCollectionInputConfiguration]]
        """
        return self._inputs
    
    @inputs.setter
    def inputs(self,value: Optional[List[authentication_attribute_collection_input_configuration.AuthenticationAttributeCollectionInputConfiguration]] = None) -> None:
        """
        Sets the inputs property value. The display configuration of attributes being collected on the attribute collection page.
        Args:
            value: Value to set for the inputs property.
        """
        self._inputs = value
    
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
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("inputs", self.inputs)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of the attribute collection page.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of the attribute collection page.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    


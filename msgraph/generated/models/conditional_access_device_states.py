from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ConditionalAccessDeviceStates(AdditionalDataHolder, Parsable):
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
        Instantiates a new conditionalAccessDeviceStates and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # States excluded from the scope of the policy. Possible values: Compliant, DomainJoined.
        self._exclude_states: Optional[List[str]] = None
        # States in the scope of the policy. All is the only allowed value.
        self._include_states: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessDeviceStates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessDeviceStates
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessDeviceStates()
    
    @property
    def exclude_states(self,) -> Optional[List[str]]:
        """
        Gets the excludeStates property value. States excluded from the scope of the policy. Possible values: Compliant, DomainJoined.
        Returns: Optional[List[str]]
        """
        return self._exclude_states
    
    @exclude_states.setter
    def exclude_states(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeStates property value. States excluded from the scope of the policy. Possible values: Compliant, DomainJoined.
        Args:
            value: Value to set for the excludeStates property.
        """
        self._exclude_states = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exclude_states": lambda n : setattr(self, 'exclude_states', n.get_collection_of_primitive_values(str)),
            "include_states": lambda n : setattr(self, 'include_states', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def include_states(self,) -> Optional[List[str]]:
        """
        Gets the includeStates property value. States in the scope of the policy. All is the only allowed value.
        Returns: Optional[List[str]]
        """
        return self._include_states
    
    @include_states.setter
    def include_states(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeStates property value. States in the scope of the policy. All is the only allowed value.
        Args:
            value: Value to set for the includeStates property.
        """
        self._include_states = value
    
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
        writer.write_collection_of_primitive_values("excludeStates", self.exclude_states)
        writer.write_collection_of_primitive_values("includeStates", self.include_states)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


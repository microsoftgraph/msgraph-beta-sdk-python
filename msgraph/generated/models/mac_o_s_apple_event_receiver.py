from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mac_o_s_process_identifier_type = lazy_import('msgraph.generated.models.mac_o_s_process_identifier_type')

class MacOSAppleEventReceiver(AdditionalDataHolder, Parsable):
    """
    Represents a process that can receive an Apple Event notification.
    """
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
    
    @property
    def allowed(self,) -> Optional[bool]:
        """
        Gets the allowed property value. Allow or block this app from receiving Apple events.
        Returns: Optional[bool]
        """
        return self._allowed
    
    @allowed.setter
    def allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowed property value. Allow or block this app from receiving Apple events.
        Args:
            value: Value to set for the allowed property.
        """
        self._allowed = value
    
    @property
    def code_requirement(self,) -> Optional[str]:
        """
        Gets the codeRequirement property value. Code requirement for the app or binary that receives the Apple Event.
        Returns: Optional[str]
        """
        return self._code_requirement
    
    @code_requirement.setter
    def code_requirement(self,value: Optional[str] = None) -> None:
        """
        Sets the codeRequirement property value. Code requirement for the app or binary that receives the Apple Event.
        Args:
            value: Value to set for the codeRequirement property.
        """
        self._code_requirement = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new macOSAppleEventReceiver and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Allow or block this app from receiving Apple events.
        self._allowed: Optional[bool] = None
        # Code requirement for the app or binary that receives the Apple Event.
        self._code_requirement: Optional[str] = None
        # Bundle ID of the app or file path of the process or executable that receives the Apple Event.
        self._identifier: Optional[str] = None
        # Process identifier types for MacOS Privacy Preferences
        self._identifier_type: Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSAppleEventReceiver:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSAppleEventReceiver
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSAppleEventReceiver()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed": lambda n : setattr(self, 'allowed', n.get_bool_value()),
            "code_requirement": lambda n : setattr(self, 'code_requirement', n.get_str_value()),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "identifier_type": lambda n : setattr(self, 'identifier_type', n.get_enum_value(mac_o_s_process_identifier_type.MacOSProcessIdentifierType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def identifier(self,) -> Optional[str]:
        """
        Gets the identifier property value. Bundle ID of the app or file path of the process or executable that receives the Apple Event.
        Returns: Optional[str]
        """
        return self._identifier
    
    @identifier.setter
    def identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identifier property value. Bundle ID of the app or file path of the process or executable that receives the Apple Event.
        Args:
            value: Value to set for the identifier property.
        """
        self._identifier = value
    
    @property
    def identifier_type(self,) -> Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType]:
        """
        Gets the identifierType property value. Process identifier types for MacOS Privacy Preferences
        Returns: Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType]
        """
        return self._identifier_type
    
    @identifier_type.setter
    def identifier_type(self,value: Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType] = None) -> None:
        """
        Sets the identifierType property value. Process identifier types for MacOS Privacy Preferences
        Args:
            value: Value to set for the identifierType property.
        """
        self._identifier_type = value
    
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
        writer.write_bool_value("allowed", self.allowed)
        writer.write_str_value("codeRequirement", self.code_requirement)
        writer.write_str_value("identifier", self.identifier)
        writer.write_enum_value("identifierType", self.identifier_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


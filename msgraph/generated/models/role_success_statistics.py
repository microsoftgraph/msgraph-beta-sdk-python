from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RoleSuccessStatistics(AdditionalDataHolder, Parsable):
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
        Instantiates a new roleSuccessStatistics and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The permanentFail property
        self._permanent_fail: Optional[int] = None
        # The permanentSuccess property
        self._permanent_success: Optional[int] = None
        # The removeFail property
        self._remove_fail: Optional[int] = None
        # The removeSuccess property
        self._remove_success: Optional[int] = None
        # The roleId property
        self._role_id: Optional[str] = None
        # The roleName property
        self._role_name: Optional[str] = None
        # The temporaryFail property
        self._temporary_fail: Optional[int] = None
        # The temporarySuccess property
        self._temporary_success: Optional[int] = None
        # The unknownFail property
        self._unknown_fail: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleSuccessStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleSuccessStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleSuccessStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permanent_fail": lambda n : setattr(self, 'permanent_fail', n.get_int_value()),
            "permanent_success": lambda n : setattr(self, 'permanent_success', n.get_int_value()),
            "remove_fail": lambda n : setattr(self, 'remove_fail', n.get_int_value()),
            "remove_success": lambda n : setattr(self, 'remove_success', n.get_int_value()),
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_name": lambda n : setattr(self, 'role_name', n.get_str_value()),
            "temporary_fail": lambda n : setattr(self, 'temporary_fail', n.get_int_value()),
            "temporary_success": lambda n : setattr(self, 'temporary_success', n.get_int_value()),
            "unknown_fail": lambda n : setattr(self, 'unknown_fail', n.get_int_value()),
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
    
    @property
    def permanent_fail(self,) -> Optional[int]:
        """
        Gets the permanentFail property value. The permanentFail property
        Returns: Optional[int]
        """
        return self._permanent_fail
    
    @permanent_fail.setter
    def permanent_fail(self,value: Optional[int] = None) -> None:
        """
        Sets the permanentFail property value. The permanentFail property
        Args:
            value: Value to set for the permanentFail property.
        """
        self._permanent_fail = value
    
    @property
    def permanent_success(self,) -> Optional[int]:
        """
        Gets the permanentSuccess property value. The permanentSuccess property
        Returns: Optional[int]
        """
        return self._permanent_success
    
    @permanent_success.setter
    def permanent_success(self,value: Optional[int] = None) -> None:
        """
        Sets the permanentSuccess property value. The permanentSuccess property
        Args:
            value: Value to set for the permanentSuccess property.
        """
        self._permanent_success = value
    
    @property
    def remove_fail(self,) -> Optional[int]:
        """
        Gets the removeFail property value. The removeFail property
        Returns: Optional[int]
        """
        return self._remove_fail
    
    @remove_fail.setter
    def remove_fail(self,value: Optional[int] = None) -> None:
        """
        Sets the removeFail property value. The removeFail property
        Args:
            value: Value to set for the removeFail property.
        """
        self._remove_fail = value
    
    @property
    def remove_success(self,) -> Optional[int]:
        """
        Gets the removeSuccess property value. The removeSuccess property
        Returns: Optional[int]
        """
        return self._remove_success
    
    @remove_success.setter
    def remove_success(self,value: Optional[int] = None) -> None:
        """
        Sets the removeSuccess property value. The removeSuccess property
        Args:
            value: Value to set for the removeSuccess property.
        """
        self._remove_success = value
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. The roleId property
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. The roleId property
        Args:
            value: Value to set for the roleId property.
        """
        self._role_id = value
    
    @property
    def role_name(self,) -> Optional[str]:
        """
        Gets the roleName property value. The roleName property
        Returns: Optional[str]
        """
        return self._role_name
    
    @role_name.setter
    def role_name(self,value: Optional[str] = None) -> None:
        """
        Sets the roleName property value. The roleName property
        Args:
            value: Value to set for the roleName property.
        """
        self._role_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("permanentFail", self.permanent_fail)
        writer.write_int_value("permanentSuccess", self.permanent_success)
        writer.write_int_value("removeFail", self.remove_fail)
        writer.write_int_value("removeSuccess", self.remove_success)
        writer.write_str_value("roleId", self.role_id)
        writer.write_str_value("roleName", self.role_name)
        writer.write_int_value("temporaryFail", self.temporary_fail)
        writer.write_int_value("temporarySuccess", self.temporary_success)
        writer.write_int_value("unknownFail", self.unknown_fail)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def temporary_fail(self,) -> Optional[int]:
        """
        Gets the temporaryFail property value. The temporaryFail property
        Returns: Optional[int]
        """
        return self._temporary_fail
    
    @temporary_fail.setter
    def temporary_fail(self,value: Optional[int] = None) -> None:
        """
        Sets the temporaryFail property value. The temporaryFail property
        Args:
            value: Value to set for the temporaryFail property.
        """
        self._temporary_fail = value
    
    @property
    def temporary_success(self,) -> Optional[int]:
        """
        Gets the temporarySuccess property value. The temporarySuccess property
        Returns: Optional[int]
        """
        return self._temporary_success
    
    @temporary_success.setter
    def temporary_success(self,value: Optional[int] = None) -> None:
        """
        Sets the temporarySuccess property value. The temporarySuccess property
        Args:
            value: Value to set for the temporarySuccess property.
        """
        self._temporary_success = value
    
    @property
    def unknown_fail(self,) -> Optional[int]:
        """
        Gets the unknownFail property value. The unknownFail property
        Returns: Optional[int]
        """
        return self._unknown_fail
    
    @unknown_fail.setter
    def unknown_fail(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownFail property value. The unknownFail property
        Args:
            value: Value to set for the unknownFail property.
        """
        self._unknown_fail = value
    


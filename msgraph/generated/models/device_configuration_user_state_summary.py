from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DeviceConfigurationUserStateSummary(entity.Entity):
    @property
    def compliant_user_count(self,) -> Optional[int]:
        """
        Gets the compliantUserCount property value. Number of compliant users
        Returns: Optional[int]
        """
        return self._compliant_user_count
    
    @compliant_user_count.setter
    def compliant_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantUserCount property value. Number of compliant users
        Args:
            value: Value to set for the compliantUserCount property.
        """
        self._compliant_user_count = value
    
    @property
    def conflict_user_count(self,) -> Optional[int]:
        """
        Gets the conflictUserCount property value. Number of conflict users
        Returns: Optional[int]
        """
        return self._conflict_user_count
    
    @conflict_user_count.setter
    def conflict_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictUserCount property value. Number of conflict users
        Args:
            value: Value to set for the conflictUserCount property.
        """
        self._conflict_user_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceConfigurationUserStateSummary and sets the default values.
        """
        super().__init__()
        # Number of compliant users
        self._compliant_user_count: Optional[int] = None
        # Number of conflict users
        self._conflict_user_count: Optional[int] = None
        # Number of error users
        self._error_user_count: Optional[int] = None
        # Number of NonCompliant users
        self._non_compliant_user_count: Optional[int] = None
        # Number of not applicable users
        self._not_applicable_user_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of remediated users
        self._remediated_user_count: Optional[int] = None
        # Number of unknown users
        self._unknown_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfigurationUserStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationUserStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceConfigurationUserStateSummary()
    
    @property
    def error_user_count(self,) -> Optional[int]:
        """
        Gets the errorUserCount property value. Number of error users
        Returns: Optional[int]
        """
        return self._error_user_count
    
    @error_user_count.setter
    def error_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorUserCount property value. Number of error users
        Args:
            value: Value to set for the errorUserCount property.
        """
        self._error_user_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliant_user_count": lambda n : setattr(self, 'compliant_user_count', n.get_int_value()),
            "conflict_user_count": lambda n : setattr(self, 'conflict_user_count', n.get_int_value()),
            "error_user_count": lambda n : setattr(self, 'error_user_count', n.get_int_value()),
            "non_compliant_user_count": lambda n : setattr(self, 'non_compliant_user_count', n.get_int_value()),
            "not_applicable_user_count": lambda n : setattr(self, 'not_applicable_user_count', n.get_int_value()),
            "remediated_user_count": lambda n : setattr(self, 'remediated_user_count', n.get_int_value()),
            "unknown_user_count": lambda n : setattr(self, 'unknown_user_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def non_compliant_user_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantUserCount property value. Number of NonCompliant users
        Returns: Optional[int]
        """
        return self._non_compliant_user_count
    
    @non_compliant_user_count.setter
    def non_compliant_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantUserCount property value. Number of NonCompliant users
        Args:
            value: Value to set for the nonCompliantUserCount property.
        """
        self._non_compliant_user_count = value
    
    @property
    def not_applicable_user_count(self,) -> Optional[int]:
        """
        Gets the notApplicableUserCount property value. Number of not applicable users
        Returns: Optional[int]
        """
        return self._not_applicable_user_count
    
    @not_applicable_user_count.setter
    def not_applicable_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableUserCount property value. Number of not applicable users
        Args:
            value: Value to set for the notApplicableUserCount property.
        """
        self._not_applicable_user_count = value
    
    @property
    def remediated_user_count(self,) -> Optional[int]:
        """
        Gets the remediatedUserCount property value. Number of remediated users
        Returns: Optional[int]
        """
        return self._remediated_user_count
    
    @remediated_user_count.setter
    def remediated_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedUserCount property value. Number of remediated users
        Args:
            value: Value to set for the remediatedUserCount property.
        """
        self._remediated_user_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("compliantUserCount", self.compliant_user_count)
        writer.write_int_value("conflictUserCount", self.conflict_user_count)
        writer.write_int_value("errorUserCount", self.error_user_count)
        writer.write_int_value("nonCompliantUserCount", self.non_compliant_user_count)
        writer.write_int_value("notApplicableUserCount", self.not_applicable_user_count)
        writer.write_int_value("remediatedUserCount", self.remediated_user_count)
        writer.write_int_value("unknownUserCount", self.unknown_user_count)
    
    @property
    def unknown_user_count(self,) -> Optional[int]:
        """
        Gets the unknownUserCount property value. Number of unknown users
        Returns: Optional[int]
        """
        return self._unknown_user_count
    
    @unknown_user_count.setter
    def unknown_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownUserCount property value. Number of unknown users
        Args:
            value: Value to set for the unknownUserCount property.
        """
        self._unknown_user_count = value
    


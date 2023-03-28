from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, security_baseline_category_state_summary

from . import entity

class SecurityBaselineStateSummary(entity.Entity):
    """
    The security baseline compliance state summary for the security baseline of the account.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new securityBaselineStateSummary and sets the default values.
        """
        super().__init__()
        # Number of conflict devices
        self._conflict_count: Optional[int] = None
        # Number of error devices
        self._error_count: Optional[int] = None
        # Number of not applicable devices
        self._not_applicable_count: Optional[int] = None
        # Number of not secure devices
        self._not_secure_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of secure devices
        self._secure_count: Optional[int] = None
        # Number of unknown devices
        self._unknown_count: Optional[int] = None
    
    @property
    def conflict_count(self,) -> Optional[int]:
        """
        Gets the conflictCount property value. Number of conflict devices
        Returns: Optional[int]
        """
        return self._conflict_count
    
    @conflict_count.setter
    def conflict_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictCount property value. Number of conflict devices
        Args:
            value: Value to set for the conflict_count property.
        """
        self._conflict_count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.securityBaselineCategoryStateSummary":
                from . import security_baseline_category_state_summary

                return security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary()
        return SecurityBaselineStateSummary()
    
    @property
    def error_count(self,) -> Optional[int]:
        """
        Gets the errorCount property value. Number of error devices
        Returns: Optional[int]
        """
        return self._error_count
    
    @error_count.setter
    def error_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCount property value. Number of error devices
        Args:
            value: Value to set for the error_count property.
        """
        self._error_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, security_baseline_category_state_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "conflictCount": lambda n : setattr(self, 'conflict_count', n.get_int_value()),
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "notApplicableCount": lambda n : setattr(self, 'not_applicable_count', n.get_int_value()),
            "notSecureCount": lambda n : setattr(self, 'not_secure_count', n.get_int_value()),
            "secureCount": lambda n : setattr(self, 'secure_count', n.get_int_value()),
            "unknownCount": lambda n : setattr(self, 'unknown_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def not_applicable_count(self,) -> Optional[int]:
        """
        Gets the notApplicableCount property value. Number of not applicable devices
        Returns: Optional[int]
        """
        return self._not_applicable_count
    
    @not_applicable_count.setter
    def not_applicable_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableCount property value. Number of not applicable devices
        Args:
            value: Value to set for the not_applicable_count property.
        """
        self._not_applicable_count = value
    
    @property
    def not_secure_count(self,) -> Optional[int]:
        """
        Gets the notSecureCount property value. Number of not secure devices
        Returns: Optional[int]
        """
        return self._not_secure_count
    
    @not_secure_count.setter
    def not_secure_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notSecureCount property value. Number of not secure devices
        Args:
            value: Value to set for the not_secure_count property.
        """
        self._not_secure_count = value
    
    @property
    def secure_count(self,) -> Optional[int]:
        """
        Gets the secureCount property value. Number of secure devices
        Returns: Optional[int]
        """
        return self._secure_count
    
    @secure_count.setter
    def secure_count(self,value: Optional[int] = None) -> None:
        """
        Sets the secureCount property value. Number of secure devices
        Args:
            value: Value to set for the secure_count property.
        """
        self._secure_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("conflictCount", self.conflict_count)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_int_value("notApplicableCount", self.not_applicable_count)
        writer.write_int_value("notSecureCount", self.not_secure_count)
        writer.write_int_value("secureCount", self.secure_count)
        writer.write_int_value("unknownCount", self.unknown_count)
    
    @property
    def unknown_count(self,) -> Optional[int]:
        """
        Gets the unknownCount property value. Number of unknown devices
        Returns: Optional[int]
        """
        return self._unknown_count
    
    @unknown_count.setter
    def unknown_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownCount property value. Number of unknown devices
        Args:
            value: Value to set for the unknown_count property.
        """
        self._unknown_count = value
    


from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_operation_status = lazy_import('msgraph.generated.models.group_policy_operation_status')
group_policy_operation_type = lazy_import('msgraph.generated.models.group_policy_operation_type')

class GroupPolicyOperation(entity.Entity):
    """
    The entity represents an group policy operation.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyOperation and sets the default values.
        """
        super().__init__()
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Type of Group Policy operation status.
        self._operation_status: Optional[group_policy_operation_status.GroupPolicyOperationStatus] = None
        # Type of Group Policy operation.
        self._operation_type: Optional[group_policy_operation_type.GroupPolicyOperationType] = None
        # The group policy operation status detail.
        self._status_details: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operation_status": lambda n : setattr(self, 'operation_status', n.get_enum_value(group_policy_operation_status.GroupPolicyOperationStatus)),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_enum_value(group_policy_operation_type.GroupPolicyOperationType)),
            "status_details": lambda n : setattr(self, 'status_details', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def operation_status(self,) -> Optional[group_policy_operation_status.GroupPolicyOperationStatus]:
        """
        Gets the operationStatus property value. Type of Group Policy operation status.
        Returns: Optional[group_policy_operation_status.GroupPolicyOperationStatus]
        """
        return self._operation_status
    
    @operation_status.setter
    def operation_status(self,value: Optional[group_policy_operation_status.GroupPolicyOperationStatus] = None) -> None:
        """
        Sets the operationStatus property value. Type of Group Policy operation status.
        Args:
            value: Value to set for the operationStatus property.
        """
        self._operation_status = value
    
    @property
    def operation_type(self,) -> Optional[group_policy_operation_type.GroupPolicyOperationType]:
        """
        Gets the operationType property value. Type of Group Policy operation.
        Returns: Optional[group_policy_operation_type.GroupPolicyOperationType]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[group_policy_operation_type.GroupPolicyOperationType] = None) -> None:
        """
        Sets the operationType property value. Type of Group Policy operation.
        Args:
            value: Value to set for the operationType property.
        """
        self._operation_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("operationStatus", self.operation_status)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_str_value("statusDetails", self.status_details)
    
    @property
    def status_details(self,) -> Optional[str]:
        """
        Gets the statusDetails property value. The group policy operation status detail.
        Returns: Optional[str]
        """
        return self._status_details
    
    @status_details.setter
    def status_details(self,value: Optional[str] = None) -> None:
        """
        Sets the statusDetails property value. The group policy operation status detail.
        Args:
            value: Value to set for the statusDetails property.
        """
        self._status_details = value
    


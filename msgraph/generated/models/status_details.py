from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

provisioning_status_error_category = lazy_import('msgraph.generated.models.provisioning_status_error_category')
status_base = lazy_import('msgraph.generated.models.status_base')

class StatusDetails(status_base.StatusBase):
    @property
    def additional_details(self,) -> Optional[str]:
        """
        Gets the additionalDetails property value. Additional details in case of error.
        Returns: Optional[str]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalDetails property value. Additional details in case of error.
        Args:
            value: Value to set for the additionalDetails property.
        """
        self._additional_details = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new StatusDetails and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.statusDetails"
        # Additional details in case of error.
        self._additional_details: Optional[str] = None
        # Categorizes the error code. Possible values are Failure, NonServiceFailure, Success.
        self._error_category: Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory] = None
        # Unique error code if any occurred. Learn more
        self._error_code: Optional[str] = None
        # Summarizes the status and describes why the status happened.
        self._reason: Optional[str] = None
        # Provides the resolution for the corresponding error.
        self._recommended_action: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StatusDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StatusDetails()
    
    @property
    def error_category(self,) -> Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory]:
        """
        Gets the errorCategory property value. Categorizes the error code. Possible values are Failure, NonServiceFailure, Success.
        Returns: Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory]
        """
        return self._error_category
    
    @error_category.setter
    def error_category(self,value: Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory] = None) -> None:
        """
        Sets the errorCategory property value. Categorizes the error code. Possible values are Failure, NonServiceFailure, Success.
        Args:
            value: Value to set for the errorCategory property.
        """
        self._error_category = value
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. Unique error code if any occurred. Learn more
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. Unique error code if any occurred. Learn more
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_details": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "error_category": lambda n : setattr(self, 'error_category', n.get_enum_value(provisioning_status_error_category.ProvisioningStatusErrorCategory)),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recommended_action": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reason(self,) -> Optional[str]:
        """
        Gets the reason property value. Summarizes the status and describes why the status happened.
        Returns: Optional[str]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[str] = None) -> None:
        """
        Sets the reason property value. Summarizes the status and describes why the status happened.
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    @property
    def recommended_action(self,) -> Optional[str]:
        """
        Gets the recommendedAction property value. Provides the resolution for the corresponding error.
        Returns: Optional[str]
        """
        return self._recommended_action
    
    @recommended_action.setter
    def recommended_action(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendedAction property value. Provides the resolution for the corresponding error.
        Args:
            value: Value to set for the recommendedAction property.
        """
        self._recommended_action = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_enum_value("errorCategory", self.error_category)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recommendedAction", self.recommended_action)
    


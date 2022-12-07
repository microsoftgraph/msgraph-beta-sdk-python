from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

membership_rule_processing_status_details = lazy_import('msgraph.generated.models.membership_rule_processing_status_details')

class MembershipRuleProcessingStatus(AdditionalDataHolder, Parsable):
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
        Instantiates a new membershipRuleProcessingStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Detailed error message if dynamic group processing ran into an error.  Optional. Read-only.
        self._error_message: Optional[str] = None
        # Most recent date and time when membership of a dynamic group was updated.  Optional. Read-only.
        self._last_membership_updated: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Current status of a dynamic group processing. Possible values are: NotStarted, Running, Succeeded, Failed, and UnknownFutureValue.  Required. Read-only.
        self._status: Optional[membership_rule_processing_status_details.MembershipRuleProcessingStatusDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MembershipRuleProcessingStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MembershipRuleProcessingStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MembershipRuleProcessingStatus()
    
    @property
    def error_message(self,) -> Optional[str]:
        """
        Gets the errorMessage property value. Detailed error message if dynamic group processing ran into an error.  Optional. Read-only.
        Returns: Optional[str]
        """
        return self._error_message
    
    @error_message.setter
    def error_message(self,value: Optional[str] = None) -> None:
        """
        Sets the errorMessage property value. Detailed error message if dynamic group processing ran into an error.  Optional. Read-only.
        Args:
            value: Value to set for the errorMessage property.
        """
        self._error_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error_message": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "last_membership_updated": lambda n : setattr(self, 'last_membership_updated', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(membership_rule_processing_status_details.MembershipRuleProcessingStatusDetails)),
        }
        return fields
    
    @property
    def last_membership_updated(self,) -> Optional[datetime]:
        """
        Gets the lastMembershipUpdated property value. Most recent date and time when membership of a dynamic group was updated.  Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_membership_updated
    
    @last_membership_updated.setter
    def last_membership_updated(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastMembershipUpdated property value. Most recent date and time when membership of a dynamic group was updated.  Optional. Read-only.
        Args:
            value: Value to set for the lastMembershipUpdated property.
        """
        self._last_membership_updated = value
    
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
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_datetime_value("lastMembershipUpdated", self.last_membership_updated)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[membership_rule_processing_status_details.MembershipRuleProcessingStatusDetails]:
        """
        Gets the status property value. Current status of a dynamic group processing. Possible values are: NotStarted, Running, Succeeded, Failed, and UnknownFutureValue.  Required. Read-only.
        Returns: Optional[membership_rule_processing_status_details.MembershipRuleProcessingStatusDetails]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[membership_rule_processing_status_details.MembershipRuleProcessingStatusDetails] = None) -> None:
        """
        Sets the status property value. Current status of a dynamic group processing. Possible values are: NotStarted, Running, Succeeded, Failed, and UnknownFutureValue.  Required. Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    


from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

workload_onboarding_status = lazy_import('msgraph.generated.models.managed_tenants.workload_onboarding_status')

class WorkloadStatus(AdditionalDataHolder, Parsable):
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
        Instantiates a new workloadStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The display name for the workload. Required. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date and time the workload was offboarded. Optional. Read-only.
        self._offboarded_date_time: Optional[datetime] = None
        # The date and time the workload was onboarded. Optional. Read-only.
        self._onboarded_date_time: Optional[datetime] = None
        # The onboardingStatus property
        self._onboarding_status: Optional[workload_onboarding_status.WorkloadOnboardingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkloadStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkloadStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkloadStatus()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the workload. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the workload. Required. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offboarded_date_time": lambda n : setattr(self, 'offboarded_date_time', n.get_datetime_value()),
            "onboarded_date_time": lambda n : setattr(self, 'onboarded_date_time', n.get_datetime_value()),
            "onboarding_status": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(workload_onboarding_status.WorkloadOnboardingStatus)),
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
    def offboarded_date_time(self,) -> Optional[datetime]:
        """
        Gets the offboardedDateTime property value. The date and time the workload was offboarded. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._offboarded_date_time
    
    @offboarded_date_time.setter
    def offboarded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the offboardedDateTime property value. The date and time the workload was offboarded. Optional. Read-only.
        Args:
            value: Value to set for the offboardedDateTime property.
        """
        self._offboarded_date_time = value
    
    @property
    def onboarded_date_time(self,) -> Optional[datetime]:
        """
        Gets the onboardedDateTime property value. The date and time the workload was onboarded. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._onboarded_date_time
    
    @onboarded_date_time.setter
    def onboarded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onboardedDateTime property value. The date and time the workload was onboarded. Optional. Read-only.
        Args:
            value: Value to set for the onboardedDateTime property.
        """
        self._onboarded_date_time = value
    
    @property
    def onboarding_status(self,) -> Optional[workload_onboarding_status.WorkloadOnboardingStatus]:
        """
        Gets the onboardingStatus property value. The onboardingStatus property
        Returns: Optional[workload_onboarding_status.WorkloadOnboardingStatus]
        """
        return self._onboarding_status
    
    @onboarding_status.setter
    def onboarding_status(self,value: Optional[workload_onboarding_status.WorkloadOnboardingStatus] = None) -> None:
        """
        Sets the onboardingStatus property value. The onboardingStatus property
        Args:
            value: Value to set for the onboardingStatus property.
        """
        self._onboarding_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("offboardedDateTime", self.offboarded_date_time)
        writer.write_datetime_value("onboardedDateTime", self.onboarded_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_additional_data_value(self.additional_data)
    


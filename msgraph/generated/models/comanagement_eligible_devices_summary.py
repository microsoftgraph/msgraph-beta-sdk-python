from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ComanagementEligibleDevicesSummary(AdditionalDataHolder, Parsable):
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
    def comanaged_count(self,) -> Optional[int]:
        """
        Gets the comanagedCount property value. Count of devices already Co-Managed
        Returns: Optional[int]
        """
        return self._comanaged_count
    
    @comanaged_count.setter
    def comanaged_count(self,value: Optional[int] = None) -> None:
        """
        Sets the comanagedCount property value. Count of devices already Co-Managed
        Args:
            value: Value to set for the comanagedCount property.
        """
        self._comanaged_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new comanagementEligibleDevicesSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Count of devices already Co-Managed
        self._comanaged_count: Optional[int] = None
        # Count of devices eligible for Co-Management but not yet joined to Azure Active Directory
        self._eligible_but_not_azure_ad_joined_count: Optional[int] = None
        # Count of devices fully eligible for Co-Management
        self._eligible_count: Optional[int] = None
        # Count of devices ineligible for Co-Management
        self._ineligible_count: Optional[int] = None
        # Count of devices that will be eligible for Co-Management after an OS update
        self._needs_os_update_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Count of devices scheduled for Co-Management enrollment. Valid values 0 to 9999999
        self._scheduled_for_enrollment_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComanagementEligibleDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ComanagementEligibleDevicesSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ComanagementEligibleDevicesSummary()
    
    @property
    def eligible_but_not_azure_ad_joined_count(self,) -> Optional[int]:
        """
        Gets the eligibleButNotAzureAdJoinedCount property value. Count of devices eligible for Co-Management but not yet joined to Azure Active Directory
        Returns: Optional[int]
        """
        return self._eligible_but_not_azure_ad_joined_count
    
    @eligible_but_not_azure_ad_joined_count.setter
    def eligible_but_not_azure_ad_joined_count(self,value: Optional[int] = None) -> None:
        """
        Sets the eligibleButNotAzureAdJoinedCount property value. Count of devices eligible for Co-Management but not yet joined to Azure Active Directory
        Args:
            value: Value to set for the eligibleButNotAzureAdJoinedCount property.
        """
        self._eligible_but_not_azure_ad_joined_count = value
    
    @property
    def eligible_count(self,) -> Optional[int]:
        """
        Gets the eligibleCount property value. Count of devices fully eligible for Co-Management
        Returns: Optional[int]
        """
        return self._eligible_count
    
    @eligible_count.setter
    def eligible_count(self,value: Optional[int] = None) -> None:
        """
        Sets the eligibleCount property value. Count of devices fully eligible for Co-Management
        Args:
            value: Value to set for the eligibleCount property.
        """
        self._eligible_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comanaged_count": lambda n : setattr(self, 'comanaged_count', n.get_int_value()),
            "eligible_but_not_azure_ad_joined_count": lambda n : setattr(self, 'eligible_but_not_azure_ad_joined_count', n.get_int_value()),
            "eligible_count": lambda n : setattr(self, 'eligible_count', n.get_int_value()),
            "ineligible_count": lambda n : setattr(self, 'ineligible_count', n.get_int_value()),
            "needs_os_update_count": lambda n : setattr(self, 'needs_os_update_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduled_for_enrollment_count": lambda n : setattr(self, 'scheduled_for_enrollment_count', n.get_int_value()),
        }
        return fields
    
    @property
    def ineligible_count(self,) -> Optional[int]:
        """
        Gets the ineligibleCount property value. Count of devices ineligible for Co-Management
        Returns: Optional[int]
        """
        return self._ineligible_count
    
    @ineligible_count.setter
    def ineligible_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ineligibleCount property value. Count of devices ineligible for Co-Management
        Args:
            value: Value to set for the ineligibleCount property.
        """
        self._ineligible_count = value
    
    @property
    def needs_os_update_count(self,) -> Optional[int]:
        """
        Gets the needsOsUpdateCount property value. Count of devices that will be eligible for Co-Management after an OS update
        Returns: Optional[int]
        """
        return self._needs_os_update_count
    
    @needs_os_update_count.setter
    def needs_os_update_count(self,value: Optional[int] = None) -> None:
        """
        Sets the needsOsUpdateCount property value. Count of devices that will be eligible for Co-Management after an OS update
        Args:
            value: Value to set for the needsOsUpdateCount property.
        """
        self._needs_os_update_count = value
    
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
    def scheduled_for_enrollment_count(self,) -> Optional[int]:
        """
        Gets the scheduledForEnrollmentCount property value. Count of devices scheduled for Co-Management enrollment. Valid values 0 to 9999999
        Returns: Optional[int]
        """
        return self._scheduled_for_enrollment_count
    
    @scheduled_for_enrollment_count.setter
    def scheduled_for_enrollment_count(self,value: Optional[int] = None) -> None:
        """
        Sets the scheduledForEnrollmentCount property value. Count of devices scheduled for Co-Management enrollment. Valid values 0 to 9999999
        Args:
            value: Value to set for the scheduledForEnrollmentCount property.
        """
        self._scheduled_for_enrollment_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("comanagedCount", self.comanaged_count)
        writer.write_int_value("eligibleButNotAzureAdJoinedCount", self.eligible_but_not_azure_ad_joined_count)
        writer.write_int_value("eligibleCount", self.eligible_count)
        writer.write_int_value("ineligibleCount", self.ineligible_count)
        writer.write_int_value("needsOsUpdateCount", self.needs_os_update_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("scheduledForEnrollmentCount", self.scheduled_for_enrollment_count)
        writer.write_additional_data_value(self.additional_data)
    


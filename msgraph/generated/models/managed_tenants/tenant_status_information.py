from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delegated_privilege_status = lazy_import('msgraph.generated.models.managed_tenants.delegated_privilege_status')
tenant_onboarding_eligibility_reason = lazy_import('msgraph.generated.models.managed_tenants.tenant_onboarding_eligibility_reason')
tenant_onboarding_status = lazy_import('msgraph.generated.models.managed_tenants.tenant_onboarding_status')
workload_status = lazy_import('msgraph.generated.models.managed_tenants.workload_status')

class TenantStatusInformation(AdditionalDataHolder, Parsable):
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
        Instantiates a new tenantStatusInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The status of the delegated admin privilege relationship between the managing entity and the managed tenant. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges. Optional. Read-only.
        self._delegated_privilege_status: Optional[delegated_privilege_status.DelegatedPrivilegeStatus] = None
        # The date and time the delegated admin privileges status was updated. Optional. Read-only.
        self._last_delegated_privilege_refresh_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The identifier for the account that offboarded the managed tenant. Optional. Read-only.
        self._offboarded_by_user_id: Optional[str] = None
        # The date and time when the managed tenant was offboarded. Optional. Read-only.
        self._offboarded_date_time: Optional[datetime] = None
        # The identifier for the account that onboarded the managed tenant. Optional. Read-only.
        self._onboarded_by_user_id: Optional[str] = None
        # The date and time when the managed tenant was onboarded. Optional. Read-only.
        self._onboarded_date_time: Optional[datetime] = None
        # The onboarding status for the managed tenant.. Possible values are: ineligible, inProcess, active, inactive, unknownFutureValue. Optional. Read-only.
        self._onboarding_status: Optional[tenant_onboarding_status.TenantOnboardingStatus] = None
        # Organization's onboarding eligibility reason in Microsoft 365 Lighthouse.. Possible values are: none, contractType, delegatedAdminPrivileges,usersCount,license and unknownFutureValue. Optional. Read-only.
        self._tenant_onboarding_eligibility_reason: Optional[tenant_onboarding_eligibility_reason.TenantOnboardingEligibilityReason] = None
        # The collection of workload statues for the managed tenant. Optional. Read-only.
        self._workload_statuses: Optional[List[workload_status.WorkloadStatus]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantStatusInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantStatusInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantStatusInformation()
    
    @property
    def delegated_privilege_status(self,) -> Optional[delegated_privilege_status.DelegatedPrivilegeStatus]:
        """
        Gets the delegatedPrivilegeStatus property value. The status of the delegated admin privilege relationship between the managing entity and the managed tenant. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges. Optional. Read-only.
        Returns: Optional[delegated_privilege_status.DelegatedPrivilegeStatus]
        """
        return self._delegated_privilege_status
    
    @delegated_privilege_status.setter
    def delegated_privilege_status(self,value: Optional[delegated_privilege_status.DelegatedPrivilegeStatus] = None) -> None:
        """
        Sets the delegatedPrivilegeStatus property value. The status of the delegated admin privilege relationship between the managing entity and the managed tenant. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges. Optional. Read-only.
        Args:
            value: Value to set for the delegatedPrivilegeStatus property.
        """
        self._delegated_privilege_status = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "delegated_privilege_status": lambda n : setattr(self, 'delegated_privilege_status', n.get_enum_value(delegated_privilege_status.DelegatedPrivilegeStatus)),
            "last_delegated_privilege_refresh_date_time": lambda n : setattr(self, 'last_delegated_privilege_refresh_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offboarded_by_user_id": lambda n : setattr(self, 'offboarded_by_user_id', n.get_str_value()),
            "offboarded_date_time": lambda n : setattr(self, 'offboarded_date_time', n.get_datetime_value()),
            "onboarded_by_user_id": lambda n : setattr(self, 'onboarded_by_user_id', n.get_str_value()),
            "onboarded_date_time": lambda n : setattr(self, 'onboarded_date_time', n.get_datetime_value()),
            "onboarding_status": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(tenant_onboarding_status.TenantOnboardingStatus)),
            "tenant_onboarding_eligibility_reason": lambda n : setattr(self, 'tenant_onboarding_eligibility_reason', n.get_enum_value(tenant_onboarding_eligibility_reason.TenantOnboardingEligibilityReason)),
            "workload_statuses": lambda n : setattr(self, 'workload_statuses', n.get_collection_of_object_values(workload_status.WorkloadStatus)),
        }
        return fields
    
    @property
    def last_delegated_privilege_refresh_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastDelegatedPrivilegeRefreshDateTime property value. The date and time the delegated admin privileges status was updated. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_delegated_privilege_refresh_date_time
    
    @last_delegated_privilege_refresh_date_time.setter
    def last_delegated_privilege_refresh_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastDelegatedPrivilegeRefreshDateTime property value. The date and time the delegated admin privileges status was updated. Optional. Read-only.
        Args:
            value: Value to set for the lastDelegatedPrivilegeRefreshDateTime property.
        """
        self._last_delegated_privilege_refresh_date_time = value
    
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
    def offboarded_by_user_id(self,) -> Optional[str]:
        """
        Gets the offboardedByUserId property value. The identifier for the account that offboarded the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._offboarded_by_user_id
    
    @offboarded_by_user_id.setter
    def offboarded_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the offboardedByUserId property value. The identifier for the account that offboarded the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the offboardedByUserId property.
        """
        self._offboarded_by_user_id = value
    
    @property
    def offboarded_date_time(self,) -> Optional[datetime]:
        """
        Gets the offboardedDateTime property value. The date and time when the managed tenant was offboarded. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._offboarded_date_time
    
    @offboarded_date_time.setter
    def offboarded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the offboardedDateTime property value. The date and time when the managed tenant was offboarded. Optional. Read-only.
        Args:
            value: Value to set for the offboardedDateTime property.
        """
        self._offboarded_date_time = value
    
    @property
    def onboarded_by_user_id(self,) -> Optional[str]:
        """
        Gets the onboardedByUserId property value. The identifier for the account that onboarded the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._onboarded_by_user_id
    
    @onboarded_by_user_id.setter
    def onboarded_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the onboardedByUserId property value. The identifier for the account that onboarded the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the onboardedByUserId property.
        """
        self._onboarded_by_user_id = value
    
    @property
    def onboarded_date_time(self,) -> Optional[datetime]:
        """
        Gets the onboardedDateTime property value. The date and time when the managed tenant was onboarded. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._onboarded_date_time
    
    @onboarded_date_time.setter
    def onboarded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onboardedDateTime property value. The date and time when the managed tenant was onboarded. Optional. Read-only.
        Args:
            value: Value to set for the onboardedDateTime property.
        """
        self._onboarded_date_time = value
    
    @property
    def onboarding_status(self,) -> Optional[tenant_onboarding_status.TenantOnboardingStatus]:
        """
        Gets the onboardingStatus property value. The onboarding status for the managed tenant.. Possible values are: ineligible, inProcess, active, inactive, unknownFutureValue. Optional. Read-only.
        Returns: Optional[tenant_onboarding_status.TenantOnboardingStatus]
        """
        return self._onboarding_status
    
    @onboarding_status.setter
    def onboarding_status(self,value: Optional[tenant_onboarding_status.TenantOnboardingStatus] = None) -> None:
        """
        Sets the onboardingStatus property value. The onboarding status for the managed tenant.. Possible values are: ineligible, inProcess, active, inactive, unknownFutureValue. Optional. Read-only.
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
        writer.write_enum_value("delegatedPrivilegeStatus", self.delegated_privilege_status)
        writer.write_datetime_value("lastDelegatedPrivilegeRefreshDateTime", self.last_delegated_privilege_refresh_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("offboardedByUserId", self.offboarded_by_user_id)
        writer.write_datetime_value("offboardedDateTime", self.offboarded_date_time)
        writer.write_str_value("onboardedByUserId", self.onboarded_by_user_id)
        writer.write_datetime_value("onboardedDateTime", self.onboarded_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_enum_value("tenantOnboardingEligibilityReason", self.tenant_onboarding_eligibility_reason)
        writer.write_collection_of_object_values("workloadStatuses", self.workload_statuses)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_onboarding_eligibility_reason(self,) -> Optional[tenant_onboarding_eligibility_reason.TenantOnboardingEligibilityReason]:
        """
        Gets the tenantOnboardingEligibilityReason property value. Organization's onboarding eligibility reason in Microsoft 365 Lighthouse.. Possible values are: none, contractType, delegatedAdminPrivileges,usersCount,license and unknownFutureValue. Optional. Read-only.
        Returns: Optional[tenant_onboarding_eligibility_reason.TenantOnboardingEligibilityReason]
        """
        return self._tenant_onboarding_eligibility_reason
    
    @tenant_onboarding_eligibility_reason.setter
    def tenant_onboarding_eligibility_reason(self,value: Optional[tenant_onboarding_eligibility_reason.TenantOnboardingEligibilityReason] = None) -> None:
        """
        Sets the tenantOnboardingEligibilityReason property value. Organization's onboarding eligibility reason in Microsoft 365 Lighthouse.. Possible values are: none, contractType, delegatedAdminPrivileges,usersCount,license and unknownFutureValue. Optional. Read-only.
        Args:
            value: Value to set for the tenantOnboardingEligibilityReason property.
        """
        self._tenant_onboarding_eligibility_reason = value
    
    @property
    def workload_statuses(self,) -> Optional[List[workload_status.WorkloadStatus]]:
        """
        Gets the workloadStatuses property value. The collection of workload statues for the managed tenant. Optional. Read-only.
        Returns: Optional[List[workload_status.WorkloadStatus]]
        """
        return self._workload_statuses
    
    @workload_statuses.setter
    def workload_statuses(self,value: Optional[List[workload_status.WorkloadStatus]] = None) -> None:
        """
        Sets the workloadStatuses property value. The collection of workload statues for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the workloadStatuses property.
        """
        self._workload_statuses = value
    


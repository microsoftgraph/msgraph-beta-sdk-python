from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_privilege_status, tenant_onboarding_eligibility_reason, tenant_onboarding_status, workload_status

@dataclass
class TenantStatusInformation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The status of the delegated admin privilege relationship between the managing entity and the managed tenant. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges. Optional. Read-only.
    delegated_privilege_status: Optional[delegated_privilege_status.DelegatedPrivilegeStatus] = None
    # The date and time the delegated admin privileges status was updated. Optional. Read-only.
    last_delegated_privilege_refresh_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier for the account that offboarded the managed tenant. Optional. Read-only.
    offboarded_by_user_id: Optional[str] = None
    # The date and time when the managed tenant was offboarded. Optional. Read-only.
    offboarded_date_time: Optional[datetime] = None
    # The identifier for the account that onboarded the managed tenant. Optional. Read-only.
    onboarded_by_user_id: Optional[str] = None
    # The date and time when the managed tenant was onboarded. Optional. Read-only.
    onboarded_date_time: Optional[datetime] = None
    # The onboarding status for the managed tenant.. Possible values are: ineligible, inProcess, active, inactive, unknownFutureValue. Optional. Read-only.
    onboarding_status: Optional[tenant_onboarding_status.TenantOnboardingStatus] = None
    # Organization's onboarding eligibility reason in Microsoft 365 Lighthouse.. Possible values are: none, contractType, delegatedAdminPrivileges,usersCount,license and unknownFutureValue. Optional. Read-only.
    tenant_onboarding_eligibility_reason: Optional[tenant_onboarding_eligibility_reason.TenantOnboardingEligibilityReason] = None
    # The collection of workload statues for the managed tenant. Optional. Read-only.
    workload_statuses: Optional[List[workload_status.WorkloadStatus]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_privilege_status, tenant_onboarding_eligibility_reason, tenant_onboarding_status, workload_status

        fields: Dict[str, Callable[[Any], None]] = {
            "delegatedPrivilegeStatus": lambda n : setattr(self, 'delegated_privilege_status', n.get_enum_value(delegated_privilege_status.DelegatedPrivilegeStatus)),
            "lastDelegatedPrivilegeRefreshDateTime": lambda n : setattr(self, 'last_delegated_privilege_refresh_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offboardedByUserId": lambda n : setattr(self, 'offboarded_by_user_id', n.get_str_value()),
            "offboardedDateTime": lambda n : setattr(self, 'offboarded_date_time', n.get_datetime_value()),
            "onboardedByUserId": lambda n : setattr(self, 'onboarded_by_user_id', n.get_str_value()),
            "onboardedDateTime": lambda n : setattr(self, 'onboarded_date_time', n.get_datetime_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(tenant_onboarding_status.TenantOnboardingStatus)),
            "tenantOnboardingEligibilityReason": lambda n : setattr(self, 'tenant_onboarding_eligibility_reason', n.get_enum_value(tenant_onboarding_eligibility_reason.TenantOnboardingEligibilityReason)),
            "workloadStatuses": lambda n : setattr(self, 'workload_statuses', n.get_collection_of_object_values(workload_status.WorkloadStatus)),
        }
        return fields
    
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
    

